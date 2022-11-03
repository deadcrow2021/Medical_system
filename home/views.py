from typing import Any
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import MODeliveryForm, ReceptionAddForm, ReceptionViewForm, RecordCreationForm, DataSamplingForm
from .models import Patient, ChangeControlLog, ReceptionNotes
from administration.models import ClinicRecomendations
from dateutil.relativedelta import relativedelta
import datetime
from .choices import CHANGETYPE
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io

def user_is_admin(user):
    return not (hasattr(user, 'doctor') or hasattr(user, 'patient'))

def user_is_patient(user):
    return hasattr(user, 'patient')

def user_is_not_patient(user):
    return not hasattr(user, 'patient')

class UserIsDoctor(UserPassesTestMixin):
    def test_func(self):
        return hasattr(self.request.user, 'doctor')

def add_log(who: User,
            whom: str,
            change_type: str,
            before: str,
            after: str) -> ChangeControlLog:
    user_type = 'доктор' if hasattr(who, 'doctor') else 'пациент' if hasattr(who, 'patient') else 'администратор'
    
    if user_type == 'доктор':
        fio = who.doctor.get_full_name()
    elif user_type == 'пациент':
        fio = who.patient.get_full_name()
    else:
        fio = f'{who.first_name} {who.last_name}'
    who_changed = f'{user_type} {fio}'
    return ChangeControlLog.objects.create(
        who_changed=who_changed,
        modified_model = whom,
        change_type=change_type,
        before=before,
        after=after,
    )

def generate_pdf(lines: list):
    buf = io.BytesIO()
    canv = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textobj = canv.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont('Times-Roman', 14)

    for i in lines:
        textobj.textLine(i)
        
    canv.drawText(textobj)
    canv.showPage()
    canv.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='sampled_patients.pdf')


observation_template_models = (
    ('appointments', 'Лист назначений' ),
    ('medications', 'Прием лекарственных препаратов во время данной беременности' ),
)


@login_required
def home_page(request):
    template_name: str = 'home/home.html'
    user: User = User.objects.get(id=request.user.id)
    docs = ClinicRecomendations.objects.all()
    # user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'
    if hasattr(user, 'doctor'): user_type = 'doctor'
    elif user.is_superuser: user_type = 'admin'
    else: user_type = 'patient'
    context = {'docs':docs }
    
    if user_type == 'doctor':
        user_account = user.doctor
        related_patients = user_account.patients.all()
        context |= { 'account': user_account, 'related_patients': related_patients }
        return render(request, template_name, context)
    elif user_type == 'patient':
        keys_names = []
        for key, val in observation_template_models:
            keys_names.append((key, val))
        user_account = user.patient
        # records = user_account.records.all()
        notes = [ReceptionViewForm(instance=x) for x in ReceptionNotes.objects.filter(patient=user_account)]
        context |= { 'notes': notes }
        context |= { 'account': user_account }#'records': records }
        context |= { 'keys_names': keys_names }
        return render(request, template_name, context)
    else:
        return render(request, template_name, context)


@login_required
def account(request):
    user: User = User.objects.get(id=request.user.id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'

    if user_type == 'doctor':
        user_account = user.doctor
        related_patients = user_account.patients.all()
        return render(request, 'home/account.html', { 'account': user_account, 'related_patients': related_patients })
    else:
        user_account = user.patient
        records = user_account.records.all()
        return render(request, 'home/account.html', { 'account': user_account, 'records': records })


@login_required
@user_passes_test(user_is_not_patient)
def data_sampling_page(request):
    lines = []
    form = DataSamplingForm()
    if request.method == 'POST':
        patients = Patient.objects.all()
        form = DataSamplingForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            if all(not x for x in [i for i in form_data.values()]):
                # add message: fill any field
                return render(request, 'home/data_sampling.html', {'form':form})

            # age = form_data['age']

            if form_data['mkb_10']:
                patients = Patient.objects.select_related().filter(card__diagnosis = form_data['mkb_10'])
            if form_data['medical_organization']:
                patients = patients.select_related().filter(doctors__med_org=form_data['medical_organization'])
            if form_data['territory']:
                patients = patients.select_related().filter(card__residence_address=form_data['territory'])
            if form_data['age']:
                patients = patients.select_related().filter(card__age=form_data['age'])
            if form_data['date_of_birth']:
                patients = patients.select_related().filter(card__date_of_birth=form_data['date_of_birth'])
            if form_data['date_of_death']:
                patients = patients.select_related().filter(pregnancy_outcome__death_time=form_data['date_of_death'])
            # if form_data['city_village']:
            #     patients = patients.filter(city_village=form_data['city_village'])

            for patient in patients:
                # may be change fields
                lines.append(f'First name: {patient.first_name}')
                lines.append(f'Last name: {patient.last_name}')
                lines.append(f'Father name: {patient.father_name}')
                lines.append('===============')
            return generate_pdf(lines)  

    return render(request, 'home/data_sampling.html', {'form':form})


@login_required
@user_passes_test(user_is_patient)
def add_selfmonitor_record(request):
    user: User = User.objects.get(id=request.user.id)
    form = RecordCreationForm()
    if request.method == 'POST':
        form = RecordCreationForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = Patient.objects.get(user=user)
            add_log(user,
                    user,
                    CHANGETYPE.Добавлена_запись_в_журнал_самонаблюдения,
                    '-',
                    f'Название: {form.cleaned_data["title"]}, Описание: {form.cleaned_data["description"]}')
            record.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'home/add_record.html', context)


class ReceptionView(LoginRequiredMixin, ListView):
    template_name: str = 'home/reception.html'
    model: ReceptionNotes = ReceptionNotes
    context_object_name: str = 'notes'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user_type = 'doctor' if hasattr(self.request.user, 'doctor') else 'patient'
        if user_type == 'doctor':
            context |= { 'notes': self.model.objects.filter(doctor=self.request.user.doctor) }
        else:
            context |= { 'notes': self.model.objects.filter(patient=self.request.user.patient) }
        return context


def reception_add_page(request: HttpRequest, profile_id: int) -> HttpResponse:
    template_name = 'home/add_reception.html'
    form_class = ReceptionAddForm
    notes = ReceptionNotes.objects.filter(patient__user__pk=profile_id)
    
    if request.method == "POST":
        form: ReceptionAddForm = form_class(request.POST)
        if form.is_valid():
            commit: ReceptionNotes = form.save(commit=False)
            doctor = commit.doctor
            commit.specialization = doctor.role
            commit.cabinet = doctor.cabinet
            commit.med_organization = doctor.med_org
            patient = User.objects.get(pk=profile_id).patient
            commit.patient = patient
            commit.visit_number = ReceptionNotes.objects.filter(doctor=doctor, patient=patient).first().visit_number + 1
            commit.save()
            # return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id }))
            notes = ReceptionNotes.objects.filter(patient__user__pk=profile_id)
            form: ReceptionAddForm = form_class()
            return render(request, template_name, { 'form': form, 'notes': notes, 'profile_id': profile_id })
        else:
            return render(request, template_name, { 'form': form, 'notes': notes, 'profile_id': profile_id })
    
    return render(request, template_name, { 'form': form_class(), 'notes': notes, 'profile_id': profile_id })


def records_page(request: HttpRequest) -> HttpResponse:
    user: User = User.objects.get(id=request.user.id)
    records = user.patient.records.all()
    template_name = 'home/records.html'
    
    return render(request, template_name, { 'records': records })


def update_mo_delivery(request: HttpRequest, profile_id: int) -> HttpResponse:
    current_user = User.objects.get(pk=profile_id)
    form = MODeliveryForm(request.POST or None, instance=current_user.patient.mo_delivery)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=(profile_id,)))
    
    return render(request, 'users/update_medical_card.html', { 'form': form, 'profile_id': profile_id })
