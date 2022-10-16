from copy import deepcopy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from datetime import timedelta
from typing import Any, Optional
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from home.forms import *
from django.urls import reverse_lazy
from home.models import Doctor, Patient, MedicalCard, PregnancyOutcome
from django.utils.crypto import get_random_string
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .search_patterns import *
import django.contrib.messages as messages
from home.views import add_log
from .mkb10 import mkb10_deseases
from home.choices import CHANGETYPE
from django.utils import timezone
import time


def user_is_doctor(user):
    return hasattr(user, 'doctor')

def user_is_not_patient(user):
    return not hasattr(user, 'patient')

class UserIsNotPatient(UserPassesTestMixin):
    def test_func(self):
        return not hasattr(self.request.user, 'patient')

class UserIsAdmin(UserPassesTestMixin):
    def test_func(self):
        user_obj = self.request.user
        return not (hasattr(user_obj, 'doctor') or hasattr(user_obj, 'patient'))

def generate_username(first_name, date):
    return f'{first_name}_{date.strftime("%d%m%Y")}'


@user_passes_test(user_is_doctor)
def add_disease(request, profile_id):
    user: User = User.objects.get(id=profile_id)
    form = DiseaseCreationForm()
    if request.method == 'POST':
        form = DiseaseCreationForm(request.POST)
        if form.is_valid():
            disease = form.save(commit=False)
            patient = Patient.objects.get(user=user)
            disease.patient = patient
            add_log(request.user,
                    f'пациент {patient.get_full_name()}',
                    CHANGETYPE.Добавлена_история_болезни,
                    '-',
                    f'Болезнь: {form.cleaned_data["disease"]};')
            disease.save()
            return HttpResponseRedirect(reverse('profile', args=(profile_id,)))
    context = { 'form': form, 'deseases': mkb10_deseases }
    return render(request, 'users/add_disease.html', context)


def follow_unfollow_patient(request):
    if request.method == 'POST':
        my_profile = Doctor.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        patient = Patient.objects.get(pk=pk)
        
        if patient in my_profile.patients.all():
            my_profile.patients.remove(patient)
            add_log(my_profile.user, f'пациент {patient.get_full_name()}', CHANGETYPE.Был_отвязан_от_доктора,
                    '-', '-')
        else:
            add_log(my_profile.user, f'пациент {patient.get_full_name()}', CHANGETYPE.Был_привязан_к_доктору,
                    '-', '-')
            my_profile.patients.add(patient)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('patients')


def profile(request: HttpRequest, profile_id):
    follow = False
    user: User = User.objects.get(id=profile_id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'
    
    # delete patient
    if request.POST:
        user_profile: User = User.objects.get(pk=profile_id)
        add_log(request.user,
                f'{user_type} {user_profile.get_full_name()}',
                CHANGETYPE.Пользователь_был_удален,
                '-',
                '-')
        user_profile.delete()
        return redirect('patients')
    
    print(f'{user_type=}')
    if user_type == "doctor":
        user_profile = user.doctor
        form = DoctorCreationForm(request.POST or None, instance=user_profile)
        return render(request, 'users/profile.html', { 'profile': user_profile, 'user_type': user_type, 'form':form })
    else:
        buttons = ((key, val[0]) for key, val in name_model.items())
        user_profile = user.patient
        if hasattr(request.user, 'doctor'):
            my_profile = Doctor.objects.get(user=request.user)
            if user_profile in my_profile.patients.all():
                follow = True
        form = PatientChangeForm(request.POST or None, instance=user_profile)
        diseases = user_profile.history.all()
        return render(request, 'users/profile.html', {
            'profile': user_profile,
            'user_type': user_type,
            'diseases': diseases,
            'form': form,
            'follow': follow,
            'buttons': buttons
        })


@user_passes_test(user_is_doctor)
def medical_card(request, profile_id):
    current_user = User.objects.get(pk=profile_id)
    form = MedicalCardForm(request.POST or None, instance=current_user.patient.card)
    
    risks = current_user.patient.card.risks.all()
    obstetric_risk_forms = [ObstetricRiskCreationForm(request.POST or None, instance=i) for i in risks]
    complication_risk_forms: list = []
    for risk in risks:
        complication_risk_forms.append([ComplicationRiskCreationForm(request.POST or None, instance=i) for i in risk.complications.all()])
    risks = list(zip(obstetric_risk_forms, complication_risk_forms))
    
    return render(request, 'users/medical_card.html', { 'form': form, 'current_user': current_user,'risks': risks, })


def update_medical_card(request, profile_id):
    current_user = User.objects.get(pk=profile_id)
    form = MedicalCardForm(request.POST or None, instance=current_user.patient.card)
    return render(request, 'users/update_medical_card.html', {'form': form})


def pregnancy_outcome(request: HttpRequest, profile_id: int):
    current_user = User.objects.get(pk=profile_id)
    # form = PregnancyOutcomeForm(request.POST or None, instance=current_user.patient.pregnancy_outcome)
    
    if request.method == 'POST':
        id = request.POST['delete_outcome']
        PregnancyOutcome.objects.get(pk=id).delete()
    
    outcomes = current_user.patient.pregnancy_outcome.all()
    forms = [PregnancyOutcomeForm(instance=outcome) for outcome in outcomes]
    return render(request, 'users/pregnancy_outcome.html', {'outcome_forms': forms, 'current_user': current_user})


def add_pregnancy_outcome(request: HttpRequest, profile_id: int, outcome_id: int):
    current_user = User.objects.get(pk=profile_id)
    
    if request.method == 'POST':
        if int(outcome_id) > 0:
            form = PregnancyOutcomeForm(request.POST, instance=PregnancyOutcome.objects.get(pk=outcome_id))
        else:
            form = PregnancyOutcomeForm(request.POST)
        
        if form.is_valid():
            if int(outcome_id) > 0:
                form.save(commit=True)
            else:
                outcome = form.save(commit=False)
                patient = Patient.objects.get(user=current_user)
                outcome.patient = patient
                outcome.save()
            return HttpResponseRedirect(reverse('pregnancy-outcome', args=(profile_id,)))
    else:
        if int(outcome_id) > 0:
            form = PregnancyOutcomeForm(instance=PregnancyOutcome.objects.get(pk=outcome_id))
        else:
            form = PregnancyOutcomeForm()
    return render(request, 'users/add_pregnancy_outcome.html', { 'form': form, 'current_user': current_user })


def pregnancy_observation_page(request, profile_id):
    current_user = User.objects.get(pk=profile_id)
    keys_names = []
    for key, val in observation_forms_models.items():
        keys_names.append((key, val[2]))
    return render(request, 'users/during_pregnancy_observation.html', {'current_user': current_user, 'keys_names': keys_names})


def update_profile(request, profile_id):
    user: User = User.objects.get(pk=profile_id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'
    before = ''
    after = ''
    
    if user_type == "doctor":
        user_profile = user.doctor
        form = DoctorCreationForm(request.POST or None, instance=user_profile)
    else:
        user_profile = user.patient
        form = PatientChangeForm(request.POST or None, instance=user_profile)
    user_before = deepcopy(user_profile.__dict__)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            for field, data in form.cleaned_data.items():
                if data != user_before[field]:
                    before += f'{field}: {user_before[field]};'
                    after += f'{field}: {form.cleaned_data[field]};'
            add_log(request.user,
                    f'{user_type} {user_profile.get_full_name()}',
                    CHANGETYPE.Изменена_личная_информация,
                    before,
                    after)
            form.save()
            return HttpResponseRedirect(reverse('profile', args=(profile_id,)))
    context = {'profile': user_profile, 'form': form}
    return render(request, 'users/update_profile.html', context)


class PatientsView(UserIsNotPatient, LoginRequiredMixin, ListView):
    paginate_by: int = 6
    model = Patient
    template_name: str = 'users/patients.html'
    context_object_name = 'users'
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        pattern: list[str] =  str(request.POST['search']).lower().split()
        match pattern:
            case longStr, :
                if len(longStr) % 2 == 1:
                    context = one_word_odd(longStr)
                else:
                    context = one_word_even(longStr)
            case name, surname, fathername:
                context = three_words(name, surname, fathername)
            case name, surname, fathername, params:
                context = four_words(name, surname, fathername, params)
            case _:
                return self.get(request)
        
        context |= { 'btn': 'Вернуться' }
        return render(request, 'users/patients.html', context)


def recent_patients(request: HttpRequest):
    patients = Patient.objects.all()
    form = PatientFilterForm()
    
    if request.method == 'POST':
        form = PatientFilterForm(request.POST or None)
        if form.is_valid():
            time_interval = form.cleaned_data['time_interval']
            offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
            today = timezone.now()
            dt = today - timedelta(seconds=offset)
            dt = dt.replace(hour=0, minute=0, second=0, microsecond=0).date()
            
            match time_interval:
                case 'd':
                    patients = patients.filter(date_updated__gte=dt,)
                case 'w':
                    week_start = dt - timedelta(days=dt.weekday())
                    patients = patients.filter(date_updated__gte=week_start,)
                case 'm':
                    mounth_start = dt - timedelta(days=dt.day-1)
                    patients = patients.filter(date_updated__gte=mounth_start,)
                case '30':
                    mounth_ago = dt - timedelta(days=30)
                    patients = patients.filter(date_updated__gte=mounth_ago,)
            
            # if form.cleaned_data['territory']:
            #     patients = request.user.doctor.patients.all()
    
    context = {'patients': patients, 'form': form}
    return render(request, 'users/recent_patients.html', context)


class RegisterView(UserIsNotPatient, LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        form2 = self.form_class(request.POST)
        if form2.is_valid():
            user: User = User()
            personal: Patient | Doctor = form2.save(commit=False)
            password = get_random_string(length=8)
            user.set_password(password)
            user.username = generate_username(personal.first_name, user.date_joined)
            user.save()
            personal.user = user
            personal.save()
            user_type = 'doctor' if hasattr(personal, 'doctor') else 'patient'
            if user_type == 'patient':
                med_card = MedicalCard()
                med_card.patient = personal
                med_card.save()
            add_log(request.user,
                    f'{user_type} {personal.get_full_name()}',
                    CHANGETYPE.Пользователь_был_создан,
                    '-',
                    '-')
            if isinstance(personal, Patient) and request.user.doctor:
                personal.doctors.add(request.user.doctor)
                personal.save()
            messages.success(request, 'Запись успешно добавлена!')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form2': form2 })


class RegisterDoctorView(UserIsAdmin, RegisterView):
    template_name = 'users/add_doctor.html'
    success_url: Optional[str] = reverse_lazy('admin-page')
    form_class = DoctorCreationForm
    
    def post(self, request, *args, **kwargs):
        return super().post(request)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = { 'form1': UserCreationForm, 'form2': DoctorCreationForm }
        return context


class RegisterPatientView(RegisterView):
    template_name = 'users/add_patient.html'
    success_url: Optional[str] = reverse_lazy('patients')
    form_class = PatientCreationForm
    
    def post(self, request, *args, **kwargs):
        return super().post(request)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= { 'form1': UserCreationForm, 'form2': PatientCreationForm }
        return context


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def appearance(request: HttpResponse, profile_id: int):
    current_user = User.objects.get(pk=profile_id)
    template_name: str = 'users/appearance.html'
    
    def get_risks() -> list:
        risks = current_user.patient.card.risks.all()
        obstetric_risk_forms = [ObstetricRiskCreationForm(instance=i) for i in risks]
        complication_risk_forms: list = []
        for risk in risks:
            complication_risk_forms.append([ComplicationRiskCreationForm(instance=i) for i in risk.complications.all()])
        return list(zip(obstetric_risk_forms, complication_risk_forms))
    
    if request.method == 'POST':
        print(f'{request.POST=}')
        print(f'{request.POST["delete_pk"][0]=}')
        obstetric_risk = ObstetricRisk.objects.get(pk=request.POST["delete_pk"])
        obstetric_risk.delete()
    
    forms = get_risks()
    return render(request, template_name, context={ 'forms' : forms, 'current_user': current_user })


def add_appearance_page(request: HttpRequest, profile_id: int):
    form_class = ObstetricRiskCreationForm
    template_name: str = "users/add_appearance.html"
    success_url: str = "add-complication"
    current_user = User.objects.get(pk=profile_id)
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            app: ObstetricRisk = form.save(commit=False)
            app.card = current_user.patient.card
            app.save()
            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id, 'obsteric_id': app.pk }))
    
    return render(request, template_name, context={ 'current_user': current_user, 'form': form_class })


def add_complication_page(request: HttpRequest, profile_id: int, obsteric_id: int):
    form_class = ComplicationRiskCreationForm
    template_name: str = "users/add_complication.html"
    success_url: str = "appearance"
    current_user = User.objects.get(pk=profile_id)
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            app: ComplicationRisk = form.save(commit=False)
            app.risk = ObstetricRisk.objects.get(pk=obsteric_id)
            app.save()
            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id }))
    
    return render(request, template_name, context={ 'current_user': current_user, 'form': form_class })


def update_complication_page(request: HttpRequest, profile_id: int, complication_id: int):
    risk = ComplicationRisk.objects.get(pk=complication_id)
    form = ComplicationRiskCreationForm(request.POST or None, instance=risk)
    template_name: str = "users/update_complication.html"
    success_url: str = "appearance"
    current_user = User.objects.get(pk=profile_id)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id }))
    
    return render(request, template_name, context={ 'current_user': current_user, 'form': form })


def patient_info_page(request, profile_id):
    current_user = User.objects.get(pk=profile_id)
    instance = PatientInformation.objects.get(patient=current_user.patient)
    form = PatientInformationForm(instance=instance)
    return render(request, 'users/patient_info.html', { 'current_user': current_user, 'form': form })


def update_patient_info_page(request, profile_id):
    current_user = User.objects.get(pk=profile_id)
    success_url = 'patient-info'
    instance = PatientInformation.objects.get(patient=current_user.patient)
    
    if request.method == "POST":
        form = PatientInformationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id }))
    else:
        form = PatientInformationForm(instance=instance)
    
    return render(request, 'users/update_patient_info.html', { 'current_user': current_user, 'form': form })


observation_forms_models = {
    'pelviometry':               ( PelviometryForm, Pelviometry, 'Пельвиометрия' ),
    'pregnant_woman_monitoring': ( PregnantWomanMonitoringForm, PregnantWomanMonitoring, 'Таблица наблюдения за беременной (скрининги)' ),
    'appointments':              ( AppointmentListForm, AppointmentList, 'Лист назначений(с 618)' ),
    'medications':               ( TakingMedicationsForm, TakingMedications, 'Прием лекарственных препаратов во время данной беременности' ),
    'antibodies':                ( AntibodiesDeterminationForm, AntibodiesDetermination, 'Антитела к бледной трепонеме' ),
    'rubella':                   ( RubellaVirusForm, RubellaVirus, 'Вирус краснухи' ),
    'antiresus_bodies':          ( AntiresusBodiesForm, AntiresusBodies, 'Антирезусные тела' ),
    'blood_analysis':            ( BloodAnalysisForm, BloodAnalysis, 'Анализ крови' ),
    'biochemical_blood':         ( BiochemicalBloodAnalysisForm, BiochemicalBloodAnalysis, 'Биохимический анализ крови' ),
    'сoagulogram':               ( CoagulogramForm, Coagulogram, 'Коагулограмма' ),
    'glucose_test':              ( GlucoseToleranceTestForm, GlucoseToleranceTest, 'Пероральный глюкозотолерантный тест, ммоль/л' ),
    'ts_hormonr':                ( ThyroidStimulatingHormoneForm, ThyroidStimulatingHormone, 'Уровень тиретропного гормона (ТТГ), мкМЕ/л' ),
    'smears':                    ( SmearsForm, Smears, 'Мазки' ),
    'bacterio_smears':           ( BacterioscopicSmearsExaminationForm, BacterioscopicSmearsExamination, 'Бактериоскопическое исследование мазков' ),
    'cervix_exam':               ( CervixCytologicalExaminationForm, CervixCytologicalExamination, 'Цитологическое исследование микропрепарата шейки матки' ),
    'urine':                     ( UrineAnalysisForm, UrineAnalysis, 'Общий анализ мочи' ),
    'urine_sowing':              ( UrineSowingForm, UrineSowing, 'Посев мочи на бессимптомную бактериурию' ),
}


def observation_template_page(request: HttpRequest, profile_id: int, model_name: str) -> HttpResponse:
    template_name: str = 'users/show_template_model.html'
    success_url: str = 'medical-card'
    exists = True
    current_user = User.objects.get(pk=profile_id)
    current_pregnancy = current_user.patient.current_pregnancy
    form = observation_forms_models[model_name][0]
    model = observation_forms_models[model_name][1]
    
    if request.method == "POST":
        to_delete = model.objects.get(pk=request.POST['delete'])
        to_delete.delete()
    
    instance = tuple(model.objects.filter(current_pregnancy=current_pregnancy))
    if (len(instance) > 0):
        forms = [form(instance=i) for i in instance]
    else:
        forms = [form]
        exists = False
    
    context = { 'current_user': current_user, 'forms': forms, 'exists': exists, 'model_name': model_name }
    return render(request, template_name, context)


def update_observation_template_page(request: HttpRequest, profile_id: int, model_name: str, model_id: int) -> HttpResponse:
    template_name: str = 'users/update_template_model.html'
    success_url: str = 'observation'
    current_user = User.objects.get(pk=profile_id)
    model = observation_forms_models[model_name][0]
    
    if request.method == "POST":
        if int(model_id) > -1:
            instance = observation_forms_models[model_name][1].objects.get(pk=model_id)
            form = model(request.POST, instance=instance)
        else:
            form = model(request.POST)
        
        if form.is_valid():
            current_pregnancy = current_user.patient.current_pregnancy
            data = form.save(commit=False)
            data.current_pregnancy = current_pregnancy
            data.save()
            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id, 'model_name': model_name }))
    
    if int(model_id) > -1:
        instance = observation_forms_models[model_name][1].objects.get(pk=model_id)
        form = model(instance=instance)
    else:
        form = model
    
    context = { 'current_user': current_user, 'form': form, 'key': model_name }
    return render(request, template_name, context)


name_model = {
    'carvix':             ( CarvixScar, CarvixScarForm ),
    'father':             ( FatherInfo, FatherInfoForm ),
    'doctor_examination': ( DoctorExaminations, DoctorExaminationsForm ),
    'pregnancy_info':     ( CurrentPregnancyinfo, CurrentPregnancyinfoForm ),
    'first_examination':  ( FirstExamination, FirstExaminationForm ),
    'ultrasound_1':       ( UltrasoundFisrtTrimester, UltrasoundFisrtTrimesterForm ),
    'risk_assessment':    ( ComprehensiveRiskAssessment, ComprehensiveRiskAssessmentForm ),
    'uzi_exam_1':         ( UltrasoundExamination_19_21, UltrasoundExamination_19_21Form ),
    'uzi_exam_2':         ( UltrasoundExamination_30_34, UltrasoundExamination_30_34Form ),
}


def profile_models_template_page(request: HttpRequest, profile_id: int, model_name: str) -> HttpResponse:
    current_user = User.objects.get(pk=profile_id)
    model = name_model[model_name][0]
    form = name_model[model_name][1]
    exists = False
    
    if request.method == "POST":
        to_delete = model.objects.get(pk=request.POST['delete'])
        to_delete.delete()
    
    instance = tuple(model.objects.filter(patient=current_user.patient))
    if (len(instance) > 0):
        forms = [form(instance=i) for i in instance]
    else:
        forms = [form]
        exists = False
    
    context = { 'current_user': current_user, 'forms': forms, 'exists': exists, 'model_name': model_name }
    return render(request, 'users/profile_models_template.html', context)


def add_profile_models_template_page(request: HttpRequest, profile_id: int, model_name: str, model_id: int) -> HttpResponse:
    current_user = User.objects.get(pk=profile_id)
    success_url = "profile-models-template"
    model = name_model[model_name][1]
    
    if request.method == "POST":
        if int(model_id) > -1:
            instance = name_model[model_name][0].objects.get(pk=model_id)
            form = model(request.POST, instance=instance)
        else:
            form = model(request.POST)
        
        if form.is_valid():
            print(f'Valid')
            patient = current_user.patient
            data = form.save(commit=False)
            data.patient = patient
            data.save()
            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id, 'model_name': model_name }))
    
    if int(model_id) > -1:
        instance = name_model[model_name][0].objects.get(pk=model_id)
        form = model(instance=instance)
    else:
        form = model
    
    context = { 'current_user': current_user, 'form': form, 'model_name': model_name }
    return render(request, 'users/add_profile_models_template.html', context)