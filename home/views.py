from typing import Any
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import MODeliveryForm, ReceptionAddForm, ReceptionViewForm, RecordCreationForm, DataSamplingForm
from .models import Patient, ChangeControlLog, ReceptionNotes, MedicalCard
from administration.models import ClinicRecomendations
from .choices import CHANGETYPE
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import date
from administration.management.commands import bot
from asgiref.sync import async_to_sync
from users.mkb10 import mkb10_deseases
from home.choices import MEDICAL_ORGANIZATION
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
    
    
    # fname = 'a010013l'

    # faceName - view a010013l.AFM file as a plain text and look at
    # row beginning with 'FontName' word (it's usually the fourth row).
    # The word after 'FontName' is the faceName ('URWGothicL-Book' in this case).
    faceName = 'URWGothicL-Book'

    # Define new Type 1 font
    # cyrFace = pdfmetrics.EmbeddedType1Face(fname+'.afm', fname+'.pfb')

    # Create a new encoding called 'CP1251'
    # cyrenc = pdfmetrics.Encoding('CP1251')

    # Fill in the tuple with Unicode glyphs in accordance with cp1251 (win1251)
    # encoding
    cp1251=(
    'afii10051', 'afii10052', 'quotesinglbase', 'afii10100', 'quotedblbase',
    'ellipsis', 'dagger', 'daggerdbl', 'Euro', 'perthousand', 'afii10058',
    'guilsinglleft', 'afii10059', 'afii10061', 'afii10060', 'afii10145',
    'afii10099', 'quoteleft', 'quoteright', 'quotedblleft', 'quotedblright',
    'bullet', 'endash', 'emdash', 'tilde', 'trademark', 'afii10106',
    'guilsinglright', 'afii10107', 'afii10109', 'afii10108', 'afii10193',
    'space', 'afii10062', 'afii10110', 'afii10057', 'currency', 'afii10050',
    'brokenbar', 'section', 'afii10023', 'copyright', 'afii10053',
    'guillemotleft', 'logicalnot', 'hyphen', 'registered', 'afii10056',
    'degree', 'plusminus', 'afii10055', 'afii10103', 'afii10098', 'mu1',
    'paragraph', 'periodcentered', 'afii10071', 'afii61352', 'afii10101',
    'guillemotright', 'afii10105', 'afii10054', 'afii10102', 'afii10104',
    'afii10017', 'afii10018', 'afii10019', 'afii10020', 'afii10021',
    'afii10022', 'afii10024', 'afii10025', 'afii10026', 'afii10027',
    'afii10028', 'afii10029', 'afii10030', 'afii10031', 'afii10032',
    'afii10033', 'afii10034', 'afii10035', 'afii10036', 'afii10037',
    'afii10038', 'afii10039', 'afii10040', 'afii10041', 'afii10042',
    'afii10043', 'afii10044', 'afii10045', 'afii10046', 'afii10047',
    'afii10048', 'afii10049', 'afii10065', 'afii10066', 'afii10067',
    'afii10068', 'afii10069', 'afii10070', 'afii10072', 'afii10073',
    'afii10074', 'afii10075', 'afii10076', 'afii10077', 'afii10078',
    'afii10079', 'afii10080', 'afii10081', 'afii10082', 'afii10083',
    'afii10084', 'afii10085', 'afii10086', 'afii10087', 'afii10088',
    'afii10089', 'afii10090', 'afii10091', 'afii10092', 'afii10093',
    'afii10094', 'afii10095', 'afii10096', 'afii10097'
    )

    # Replace glyphs from code 128 to code 256 with cp1251 values
    # for i in range(128,256):
    #     cyrenc[i] = cp1251[i-128]

    # Register newly created encoding
    # pdfmetrics.registerEncoding(cyrenc)

    # Register type face
    # pdfmetrics.registerTypeFace(cyrFace)

    # Register the font with adding '1251' to its name
    # pdfmetrics.registerFont(pdfmetrics.Font(faceName+'1251', faceName, 'CP1251'))

    # Use this font and set font size
    # canv.setFont(faceName+'1251', 14)
    
    
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


def sum_risk_values(risk_objs):
    return sum([int(x.risk_value) for x in risk_objs])


def calc_preeclampsia(user_profile: Patient) -> str:
    try:
        last_monitoring = user_profile.current_pregnancy.pregnant_woman_monitoring.latest('id')
        if any((int(last_monitoring.gestation_period_weeks) and (int(last_monitoring.blood_pressure_diastolic) >= 90)),
                int(last_monitoring.systolic_blood_pressure) >= 140,
                int(last_monitoring.protein_in_urine) >= 300):
            return 'Высокий'
        else:
            return 'Низкий'
    except:
        return 'Недостаточно данных'


def calc_premature_birth(user_profile: Patient) -> str:
    try:
        last_pregnancy = user_profile.pregnancy_info.latest('id')
        if  any(any(x.outcome in ('1', '4') for x in user_profile.previous_pregnancy.all()),
                user_profile.card.age >= 35,
                (any(x <= 25 for x in user_profile.first_examination.all()) and last_pregnancy.gestation_period >= 24),
                last_pregnancy.pregnancy == '4',
                last_pregnancy.pregnancy_1 == '2',
                user_profile.patient_information.latest('id').sti):
            return 'Высокий'
        else:
            return 'Низкий'
    except:
        return 'Недостаточно данных'


def calc_risk_values_sum(user_profile: Patient) -> str | int:
    try:
        for risk in user_profile.card.risks.all():
            visit = risk.visit
            if visit == '30-40':
                return sum_risk_values(risk.complications.all())
            elif visit == '18-20':
                return sum_risk_values(risk.complications.all())
            elif visit == '11-14':
                return sum_risk_values(risk.complications.all())
            elif visit == '1':
                return sum_risk_values(risk.complications.all())
            else:
                return 0
        return 'Недостаточно данных'
    except:
        return 'Введено не числовое значение'


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
        related_patients = user_account.patients.select_related('card').all()
        risks = ((calc_preeclampsia(x), calc_premature_birth(x), calc_risk_values_sum(x))\
                for x in related_patients)
        pats = zip(related_patients, risks)
        context |= { 'account': user_account, 'pats': pats, 'cnt': len(related_patients) }
        return render(request, template_name, context)
    elif user_type == 'patient':
        keys_names = []
        for key, val in observation_template_models:
            keys_names.append((key, val))
        user_account = user.patient
        # records = user_account.records.all()
        notes = (ReceptionViewForm(instance=x) for x in ReceptionNotes.objects.filter(patient=user_account))
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
        cards = MedicalCard.objects.select_related('patient')
        form = DataSamplingForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            
            if all(not x for x in [i for i in form_data.values()]):
                # add message: fill any field
                return render(request, 'home/data_sampling.html', {'form':form , 'mkb_10': mkb10_deseases, 'med_org': med_org })
            
            # age = form_data['age']
            
            if form_data['mkb_10']:
                cards = cards.filter(diagnosis = form_data['mkb_10'])
            if form_data['medical_organization']:
                cards = cards.filter(med_org=form_data['medical_organization'])
            if form_data['territory'] and form_data['territory'] != '':
                cards = cards.filter(residence_address=form_data['territory'])
            if form_data['age']:
                cards = cards.filter(age=form_data['age'])
            if form_data['date_of_birth']:
                cards = cards.filter(date_of_birth=form_data['date_of_birth'])
            if form_data['date_of_death']:
                cards = cards.filter(patient__pregnancy_outcome__death_time=form_data['date_of_death'])
            
            if len(cards) < 1:
                return render(request, 'home/data_sampling.html', {'form':form, 'nodata': "Не найдено записей с такими данными", 'mkb_10': mkb10_deseases, 'med_org': med_org })
            
            for card in cards:
                # may be change fields
                lines.append(f'Name: {card.first_name}')
                lines.append(f'Last name: {card.last_name}')
                lines.append(f'Fathername: {card.father_name}')
                lines.append(f'Diagnosis: {card.diagnosis}')
                lines.append(f'Medical organization: {card.med_org}')
                lines.append(f'Residential address: {card.residence_address}')
                lines.append(f'Age: {card.age}')
                lines.append(f'Date of birth: {card.date_of_birth}')
                lines.append('===============')
            return generate_pdf(lines)
    med_org = ';'.join(tuple(x[1] for x in MEDICAL_ORGANIZATION[1:]))
    # med_org = tuple(x[1] for x in MEDICAL_ORGANIZATION)
    return render(request, 'home/data_sampling.html', { 'form': form, 'mkb_10': mkb10_deseases, 'med_org': med_org })


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
            return redirect('records')
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
    rolesR = ('assistant', )
    rolesNA = ('receptionist', )
    context = { 'profile_id': profile_id, 'rolesR': rolesR, 'rolesNA': rolesNA }
    
    if request.method == "POST":
        delete_id = request.POST.get('delete_id', None)
        if delete_id is not None:
            ReceptionNotes.objects.get(pk=delete_id).delete()
            notes = ReceptionNotes.objects.filter(patient__user__pk=profile_id)
            context.update({ 'form': form_class(), 'notes': notes })
            return render(request, template_name, context)
        
        form: ReceptionAddForm = form_class(request.POST)
        if form.is_valid():
            commit: ReceptionNotes = form.save(commit=False)
            doctor = commit.doctor
            commit.specialization = doctor.role
            commit.cabinet = doctor.cabinet
            commit.med_organization = doctor.med_org
            patient = User.objects.get(pk=profile_id).patient
            commit.patient = patient
            reception_note = ReceptionNotes.objects.filter(doctor=doctor, patient=patient).first()
            if reception_note is not None and reception_note.visit_number is not None:
                commit.visit_number = reception_note.visit_number + 1
            else:
                commit.visit_number = 1
            commit.save()
            # bot
            try:
                async_to_sync(bot.bot.send_message)(patient.telegramusers.tg_user_id,
                        f'Добавлена запись посещения на {commit.date_created.strftime("%d.%m.%y %H:%M")} к доктору {doctor.get_full_name()}')
            except:
                pass
            form: ReceptionAddForm = form_class()
        notes = ReceptionNotes.objects.filter(patient__user__pk=profile_id)
        context.update({ 'form': form, 'notes': notes })
        return render(request, template_name, context)
    
    notes = ReceptionNotes.objects.filter(patient__user__pk=profile_id)
    context.update({ 'form': form_class(), 'notes': notes })
    return render(request, template_name, context)


def update_reception_page(request: HttpRequest, profile_id: int, note_id: int) -> HttpResponse:
    template_name: str = 'home/update_reception.html'
    form_class = ReceptionAddForm
    
    if request.method == "POST":
        form: ReceptionAddForm = form_class(request.POST, instance=ReceptionNotes.objects.get(pk=note_id))
        if form.is_valid():
            form.save()
            request.method = "GET"
            return reception_add_page(request, profile_id)
    
    form: ReceptionAddForm = form_class(instance=ReceptionNotes.objects.get(pk=note_id))
    return render(request, template_name, { 'form': form })


def records_page(request: HttpRequest) -> HttpResponse:
    user: User = User.objects.get(pk=request.user.id)
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
    
    return render(request, 'home/mo_delivery_update.html', { 'form': form, 'profile_id': profile_id })
