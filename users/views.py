from copy import deepcopy
import med_system.settings as settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from datetime import timedelta
from datetime import date
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
from .search_patterns import *
import django.contrib.messages as messages
from home.views import add_log
from .mkb10 import mkb10_deseases
from home.choices import CHANGETYPE
from django.utils import timezone
from django.core.mail import send_mail
from .generate_samd import *
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


def translate_name(name):
    from .letter_vocabulary import VOCABULARY
    new = ''
    for letter in name:
        if letter in VOCABULARY:
            new += VOCABULARY[letter]
        else:
            new += letter
    return new


def sum_risk_values(risk_objs):
    return sum([int(x.risk_value) for x in risk_objs])



def add_disease(request, profile_id):
    # user: User = User.objects.get(id=profile_id)
    form = DiseaseCreationForm()
    if request.method == 'POST':
        form = DiseaseCreationForm(request.POST)
        if form.is_valid():
            disease = form.save(commit=False)
            patient = Patient.objects.get(user__id=profile_id)
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
    template_name: str = 'users/profile.html'
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
    
    if user_type == "doctor":
        user_profile = user.doctor
        form = DoctorCreationForm(request.POST or None, instance=user_profile)
        notes = ReceptionNotes.objects.filter(doctor=user.doctor)
        return render(request, template_name, { 'profile': user_profile, 'user_type': user_type, 'notes':notes, 'form':form })
    else:
        buttons = {(key, val[2]) for key, val in name_model.items()}
        examinations = {(key, val[2]) for key, val in doctors_examinations.items()}
        user_profile = user.patient
        if hasattr(request.user, 'doctor'):
            my_profile = Doctor.objects.get(user=request.user)
            if user_profile in my_profile.patients.all():
                follow = True
            else:
                follow = False
        form = PatientChangeForm(request.POST or None, instance=user_profile)
        diseases = user_profile.history.all()
        notes = ReceptionNotes.objects.filter(patient=user.patient)
        mo_delivery = user_profile.mo_delivery

        med_card = user_profile.card
        gestation_period = med_card.gestation_period_weeks
        date_of_birth = med_card.date_of_birth
        residence_address = med_card.residence_address

        try:
            treating_doctor = user.patient.doctors.all()[0].get_full_name()
        except:
            treating_doctor = 'Нет врача'

        try:
            last_monitoring = user_profile.current_pregnancy.pregnant_woman_monitoring.latest('id')
            if any((int(last_monitoring.gestation_period_weeks) and (int(last_monitoring.blood_pressure_diastolic) >= 90)),
                    int(last_monitoring.systolic_blood_pressure) >= 140,
                    int(last_monitoring.protein_in_urine) >= 300):
                preeclampsia = 'Высокий'
            else:
                preeclampsia = 'Низкий'
        except:
            preeclampsia = 'Недостаточно данных'

        try:
            last_pregnancy = user_profile.pregnancy_info.latest('id')
            if  any(any(x.outcome in ('1', '4') for x in user_profile.previous_pregnancy.all()),
                    user_profile.card.age >= 35,
                    (any(x <= 25 for x in user_profile.first_examination.all()) and last_pregnancy.gestation_period >= 24),
                    last_pregnancy.pregnancy == '4',
                    last_pregnancy.pregnancy_1 == '2',
                    user_profile.patient_information.latest('id').sti):
                premature_birth = 'Высокий'
            else:
                premature_birth = 'Низкий'
        except:
            premature_birth = 'Недостаточно данных'

        try:
            risk_values_sum = 0
            for risk in user_profile.card.risks.all():
                visit = risk.visit
                if visit == '30-40':
                    risk_values_sum = sum_risk_values(risk.complications.all())
                elif visit == '18-20':
                    risk_values_sum = sum_risk_values(risk.complications.all())
                elif visit == '11-14':
                    risk_values_sum = sum_risk_values(risk.complications.all())
                elif visit == '1':
                    risk_values_sum = sum_risk_values(risk.complications.all())
                else:
                    risk_values_sum = 0
        except:
            risk_values_sum = 'Введено не числовое значение'
        
        risks = (
            ('Преэклампсия',               preeclampsia),
            ('Преждевременные роды',       premature_birth),
            ('Баллы перинатального риска', risk_values_sum),
            ('Лечащий врач',               treating_doctor),
            ('Срок беременности',          gestation_period),
            ('Дата рождения',              date_of_birth),
            ('Адрес проживания',           residence_address),
            ('МО родоразрешения',          mo_delivery),
        )
        
        return render(request, template_name, {
            'profile':           user_profile,
            'user_type':         user_type,
            'diseases':          diseases,
            'form':              form,
            'follow':            follow,
            'buttons':           buttons,
            'examinations':      examinations,
            'notes':             notes,
            'risks':             risks
            # 'preeclampsia':      preeclampsia,
            # 'mo_delivery':       mo_delivery,
            # 'premature_birth':   premature_birth,
            # 'risk_values_sum':   risk_values_sum,
            # 'treating_doctor':   treating_doctor,
            # 'gestation_period':  gestation_period,
            # 'date_of_birth':     date_of_birth,
            # 'residence_address': residence_address,
        })


def self_monitoring(request: HttpResponse, profile_id: int) -> HttpResponse:
    user: User = User.objects.get(id=profile_id)
    records = user.patient.records.all()
    exists: bool = True if len(records) > 0 else False
    return render(request, 'users/self_monitoring.html', { 'curent_user': user, 'records': records, 'exists': exists })


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


def update_medical_card(request: HttpRequest, profile_id: int) -> HttpResponse:
    current_user = User.objects.get(pk=profile_id)
    form = MedicalCardForm(request.POST or None, instance=current_user.patient.card)
    
    if request.method == "POST":
        if form.is_valid():
            
            data = form.save(commit=False)
            date_of_birth = form.cleaned_data['date_of_birth']
            today = date.today()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            data.age = age
            data.save()
            return HttpResponseRedirect(reverse('medical-card', args=(profile_id,)))
    
    return render(request, 'users/update_medical_card.html', { 'form': form, 'profile_id': profile_id })


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
    for key, val in observation_template_models.items():
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
    paginate_by: int = 4
    model = Patient
    template_name: str = 'users/patients.html'
    context_object_name = 'users'
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        pattern: list[str] =  str(request.POST['search']).lower().split()
        try:
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
        except Exception as ex:
            return render(request, self.template_name, { 'error': ' '.join(pattern), 'btn': 'Вернуться' })
        
        context |= { 'btn': 'Вернуться' }
        return render(request, self.template_name, context)


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


def clear_phone(phone: str) -> str:
    ans = ''.join(c for c in phone if c.isdigit())
    return "+" + ans


class RegisterView(UserIsNotPatient, LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        post |= { 'telephone': [clear_phone(post['telephone'])] }
        form = self.form_class(post)
        if form.is_valid():
            user: User = User()
            personal: Patient | Doctor = form.save(commit=False)
            password = get_random_string(length=8)
            user.set_password(password)
            last_name = translate_name(personal.last_name)
            user.username = generate_username(last_name, user.date_joined)
            send_mail('Данные для входа в систему',
                      f'Ваши данные для входа в систему.\nЛогин: {user.username}\nПароль: {password}',
                      settings.EMAIL_HOST_USER,
                      [form.cleaned_data['email']])
            user.save()
            personal.user = user
            personal.save()
            
            user_type = 'doctor' if self.form_class == DoctorCreationForm else 'patient'
            if user_type == 'patient':
                med_card = MedicalCard()
                med_card.patient = personal
                med_card.home_phone = personal.telephone
                med_card.save()
                
                pat_info = PatientInformation()
                pat_info.patient = personal
                pat_info.save()
                
                current_preg = CurrentPregnancy()
                current_preg.patient = personal
                current_preg.save()
            
                mo_delivery = MODelivery()
                mo_delivery.patient = personal
                mo_delivery.save()

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
            return render(request, self.template_name, { 'form': form })


class RegisterDoctorView(UserIsAdmin, RegisterView):
    template_name = 'users/add_doctor.html'
    success_url: Optional[str] = reverse_lazy('admin-page')
    form_class = DoctorCreationForm
    
    def post(self, request, *args, **kwargs):
        return super().post(request)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= { 'form': DoctorCreationForm }
        return context


class RegisterPatientView(RegisterView):
    template_name = 'users/add_patient.html'
    success_url: Optional[str] = reverse_lazy('patients')
    form_class = PatientCreationForm
    
    def post(self, request, *args, **kwargs):
        return super().post(request)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= { 'form': PatientCreationForm }
        return context


def login_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        email = request.POST.get('email', None)
        if email is not None:
            msg = ""
            user = Doctor.objects.filter(email=email)
            if len(user) != 1:
                user = Patient.objects.filter(email=email)
            if len(user) != 1:
                msg = "Указанный email не был найден в базе данных"
                return render(request, 'users/login.html', { 'msg': msg })
            
            user = user[0].user
            password = get_random_string(length=8)
            user.set_password(password)
            user.save()
            send_mail('Восстановление данных',
                      f'Ваши данные для входа в систему.\nЛогин: {user.username}\nПароль: {password}',
                      settings.EMAIL_HOST_USER,
                      [email])
            return render(request, 'users/login.html')
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


patinet_info_models = {
    'previous_pregnancy': ( PreviousPregnancy, PreviousPregnancyForm, 'История предыдущих беременностей'),
    'carvix':             ( CarvixScar, CarvixScarForm, 'Сведения о рубце на матке' ),
    'father':             ( FatherInfo, FatherInfoForm, 'Сведения об отце ребенка' ),
}


def patient_info_page(request, profile_id):
    current_user = User.objects.get(pk=profile_id)
    instance = PatientInformation.objects.get(patient=current_user.patient)
    form = PatientInformationForm(instance=instance)
    key_value = ((key, val[2]) for key, val in patinet_info_models.items())
    return render(request, 'users/patient_info.html', { 'current_user': current_user, 'form': form, 'key_val': key_value })


def update_patient_info_page(request, profile_id):
    current_user = User.objects.get(pk=profile_id)
    success_url = 'patient-info'
    instance = PatientInformation.objects.get(patient=current_user.patient)
    
    if request.method == "POST":
        form = PatientInformationForm(request.POST, instance=instance)
        if form.is_valid():

            data = form.save(commit=False)
            data.imt = form.cleaned_data['mass'] / ((form.cleaned_data['height'] / 100) ** 2)
            data.save()

            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id }))
    else:
        form = PatientInformationForm(instance=instance)
    
    return render(request, 'users/update_patient_info.html', { 'current_user': current_user, 'form': form })


observation_template_models = {
    'appointments':              ( AppointmentListForm, AppointmentList, 'Лист назначений' ),
    'medications':               ( TakingMedicationsForm, TakingMedications, 'Прием лекарственных препаратов во время данной беременности' ),
}

pregnant_woman_monitoring_models = {
    'pelviometry':               ( PelviometryForm, Pelviometry, 'Пельвиометрия' ),
    'pregnant_woman_monitoring': ( PregnantWomanMonitoringForm, PregnantWomanMonitoring, 'Наблюдение за беременной' ),
}

examination_list_models = {
    'blood_analysis':            ( BloodAnalysisForm, BloodAnalysis, 'Анализ крови' ),
    'biochemical_blood':         ( BiochemicalBloodAnalysisForm, BiochemicalBloodAnalysis, 'Биохимический анализ крови' ),
    'сoagulogram':               ( CoagulogramForm, Coagulogram, 'Коагулограмма' ),
    'glucose_test':              ( GlucoseToleranceTestForm, GlucoseToleranceTest, 'Пероральный глюкозотолерантный тест, ммоль/л' ),
    'ts_hormonr':                ( ThyroidStimulatingHormoneForm, ThyroidStimulatingHormone, 'Уровень тиретропного гормона (ТТГ), мкМЕ/л' ),
    'smears':                    ( SmearsForm, Smears, 'Определение стрептококка группы B (S. agalactiae) в отделяемом цервикального канала или ректовагинальном отделяемом' ),
    'bacterio_smears':           ( BacterioscopicSmearsExaminationForm, BacterioscopicSmearsExamination, 'Бактериоскопическое исследование мазков' ),
    'cervix_exam':               ( CervixCytologicalExaminationForm, CervixCytologicalExamination, 'Цитологическое исследование микропрепарата шейки матки' ),
    'urine':                     ( UrineAnalysisForm, UrineAnalysis, 'Общий анализ мочи' ),
    'urine_sowing':              ( UrineSowingForm, UrineSowing, 'Посев мочи на бессимптомную бактериурию' ),
}

determine_antibodies = {
    'antibodies':                ( AntibodiesDeterminationForm, AntibodiesDetermination, 'Антитела к бледной трепонеме' ),
    'rubella':                   ( RubellaVirusForm, RubellaVirus, 'Вирус краснухи' ),
    'antiresus_bodies':          ( AntiresusBodiesForm, AntiresusBodies, 'Антирезусные тела' ),
}

ultrasound_models = {
    'ultrasound_1':       ( UltrasoundFisrtTrimester, UltrasoundFisrtTrimesterForm, 'Узи 1 триместра' ),
    'risk_assessment':    ( ComprehensiveRiskAssessment, ComprehensiveRiskAssessmentForm, 'Комплексная оценка рисков (11-14 недель)' ),
    'uzi_exam_1':         ( UltrasoundExamination_19_21, UltrasoundExamination_19_21Form, 'Ультразвуковое обследование (19-21 недели)' ),
    'uzi_exam_2':         ( UltrasoundExamination_30_34, UltrasoundExamination_30_34Form, 'Ультразвуковое обследование (30-34 недели)' ),
}

doctors_examinations_models = {
    'therapist': ( DoctorExaminationsTherapist, DoctorExaminationsTherapistForm, 'Осмотры терапевта' ), ######
    'dentist': ( DoctorExaminationsDentist, DoctorExaminationsDentistForm, 'Осмотры дантиста' ), ######
}

current_pregnancy_models = {
    'pregnancy_info':     ( CurrentPregnancyinfo, CurrentPregnancyinfoForm, 'Сведения о настоящей беременности' ),
    'first_examination':  ( FirstExamination, FirstExaminationForm, 'Первое обследование беременной' ),
}

portion_models = {
    'pregnant_woman_monitoring': pregnant_woman_monitoring_models,
    'examination_list':          examination_list_models,
    'determine_antibodies':      determine_antibodies,
    'ultrasound':                ultrasound_models,
    'doctors_examinations':      doctors_examinations_models,
    'current_pregnancy':         current_pregnancy_models
}

def portion_models_template_page(request: HttpRequest, profile_id: int, template_name: str, portion_name: str):
    current_user: User = User.objects.get(pk=profile_id)
    template_name = 'users/' + template_name + '.html'
    keys_names = ((key, name[2]) for key, name in portion_models[portion_name].items())
    return render(request, template_name, { 'current_user': current_user, 'keys_names': keys_names })


observation_forms_models = {
    'pelviometry':               ( PelviometryForm, Pelviometry, 'Пельвиометрия' ), #####
    'pregnant_woman_monitoring': ( PregnantWomanMonitoringForm, PregnantWomanMonitoring, 'Наблюдение за беременной' ), #####
    'appointments':              ( AppointmentListForm, AppointmentList, 'Лист назначений' ), #####
    'medications':               ( TakingMedicationsForm, TakingMedications, 'Прием лекарственных препаратов во время данной беременности' ), #####
    'antibodies':                ( AntibodiesDeterminationForm, AntibodiesDetermination, 'Антитела к бледной трепонеме' ), #####
    'rubella':                   ( RubellaVirusForm, RubellaVirus, 'Вирус краснухи' ), #####
    'antiresus_bodies':          ( AntiresusBodiesForm, AntiresusBodies, 'Антирезусные тела' ), #####
    'blood_analysis':            ( BloodAnalysisForm, BloodAnalysis, 'Анализ крови' ), #####
    'biochemical_blood':         ( BiochemicalBloodAnalysisForm, BiochemicalBloodAnalysis, 'Биохимический анализ крови' ), #####
    'сoagulogram':               ( CoagulogramForm, Coagulogram, 'Коагулограмма' ), #####
    'glucose_test':              ( GlucoseToleranceTestForm, GlucoseToleranceTest, 'Пероральный глюкозотолерантный тест, ммоль/л' ), #####
    'ts_hormonr':                ( ThyroidStimulatingHormoneForm, ThyroidStimulatingHormone, 'Уровень тиретропного гормона (ТТГ), мкМЕ/л' ), #####
    'smears':                    ( SmearsForm, Smears, 'Определение стрептококка группы B (S. agalactiae) в отделяемом цервикального канала или ректовагинальном отделяемом' ), #####
    'bacterio_smears':           ( BacterioscopicSmearsExaminationForm, BacterioscopicSmearsExamination, 'Бактериоскопическое исследование мазков' ), #####
    'cervix_exam':               ( CervixCytologicalExaminationForm, CervixCytologicalExamination, 'Цитологическое исследование микропрепарата шейки матки' ), #####
    'urine':                     ( UrineAnalysisForm, UrineAnalysis, 'Общий анализ мочи' ), #####
    'urine_sowing':              ( UrineSowingForm, UrineSowing, 'Посев мочи на бессимптомную бактериурию' ), #####
}


def observation_template_page(request: HttpRequest, profile_id: int, model_name: str) -> HttpResponse:
    template_name: str = 'users/show_template_model.html'
    # success_url: str = 'medical-card'
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
    
    context = { 'current_user': current_user, 'forms': forms, 'exists': exists, 'model_name': model_name, 'page_name': observation_forms_models[model_name][2] }
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
    
    context = { 'current_user': current_user, 'form': form, 'key': model_name, 'page_name': observation_forms_models[model_name][2] }
    return render(request, template_name, context)


name_model = {
    'previous_pregnancy': ( PreviousPregnancy, PreviousPregnancyForm, 'История предыдущих беременностей'), #####
    'carvix':             ( CarvixScar, CarvixScarForm, 'Седения о рубце на матке' ), #####
    'father':             ( FatherInfo, FatherInfoForm, 'Сведения об отце ребенка' ), #####
    'pregnancy_info':     ( CurrentPregnancyinfo, CurrentPregnancyinfoForm, 'Сведения о настоящей беременности' ), ######
    'first_examination':  ( FirstExamination, FirstExaminationForm, 'Первое обследование беременной' ), ######
    # 'shedule':            ( TurnoutSchedule, TurnoutScheduleForm, 'График явок' ),
    'hospitalization':    ( HospitalizationInformation, HospitalizationInformationForm, 'Сведения о госпитализации во время беременности' ), #####
    'ultrasound_1':       ( UltrasoundFisrtTrimester, UltrasoundFisrtTrimesterForm, 'Узи 1 триместра' ), #####
    'risk_assessment':    ( ComprehensiveRiskAssessment, ComprehensiveRiskAssessmentForm, 'Комплексная оценка рисков (11-14 недель)' ), #####
    'uzi_exam_1':         ( UltrasoundExamination_19_21, UltrasoundExamination_19_21Form, 'Ультразвуковое обследование (19-21 недели)' ), #####
    'uzi_exam_2':         ( UltrasoundExamination_30_34, UltrasoundExamination_30_34Form, 'Ультразвуковое обследование (30-34 недели)' ), #####
}


def profile_models_template_page(request: HttpRequest, profile_id: int, model_name: str) -> HttpResponse:
    current_user = User.objects.get(pk=profile_id)
    model = name_model[model_name][0]
    form = name_model[model_name][1]
    exists = True
    
    if request.method == "POST":
        to_delete = model.objects.get(pk=request.POST['delete'])
        to_delete.delete()
    
    instances = tuple(model.objects.filter(patient=current_user.patient))
    if (len(instances) > 0):
        forms = [form(instance=i) for i in instances]
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
            patient = current_user.patient
            data = form.save(commit=False)
            
            if model_name == 'father':
                mass = form.cleaned_data.get('mass')
                height = form.cleaned_data.get('height')
                if mass is not None and height is not None:
                    data.imt = mass / ((height / 100) ** 2)
                else:
                    data.imt = 0
            
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


doctors_examinations = {
    'therapist': ( DoctorExaminationsTherapist, DoctorExaminationsTherapistForm, 'Осмотры терапевта' ), ######
    'dentist': ( DoctorExaminationsDentist, DoctorExaminationsDentistForm, 'Осмотры дантиста' ), ######
}

def examination_template_page(request: HttpRequest, profile_id: int, model_name: str) -> HttpResponse:
    current_user = User.objects.get(pk=profile_id)
    model = doctors_examinations[model_name][0]
    form = doctors_examinations[model_name][1]
    exists = True
    
    if request.method == "POST":
        to_delete = model.objects.get(pk=request.POST['delete'])
        to_delete.delete()
    
    instances = tuple(model.objects.filter(patient=current_user.patient))
    if (len(instances) > 0):
        forms = [form(instance=i) for i in instances]
    else:
        forms = [form]
        exists = False
    
    context = { 'current_user': current_user, 'forms': forms, 'exists': exists, 'model_name': model_name }
    return render(request, 'users/examination_template.html', context)


def add_examination_template_page(request: HttpRequest, profile_id: int, model_name: str, model_id: int) -> HttpResponse:
    current_user = User.objects.get(pk=profile_id)
    success_url = "examination-template-page"
    model = doctors_examinations[model_name][1]
    
    if request.method == "POST":
        if int(model_id) > -1:
            instance = doctors_examinations[model_name][0].objects.get(pk=model_id)
            form = model(request.POST, instance=instance)
        else:
            form = model(request.POST)
        
        if form.is_valid():
            patient = current_user.patient
            data = form.save(commit=False)
            data.patient = patient
            data.save()
            return HttpResponseRedirect(reverse(success_url, kwargs={ 'profile_id': profile_id, 'model_name': model_name }))
    
    if int(model_id) > -1:
        instance = doctors_examinations[model_name][0].objects.get(pk=model_id)
        form = model(instance=instance)
    else:
        form = model
    
    context = { 'current_user': current_user, 'form': form, 'model_name': model_name }
    return render(request, 'users/add_examination_template.html', context)


def statistics_page(request: HttpRequest) -> HttpResponse:
    template_name: str = 'users/statistics.html'
    patients = Patient.objects.all()
    form = StatisticsPeriodForm()
    patients_number = len(patients)

    age_15_45 = 0
    age_less_18 = 0
    birth_number = 0
    birth_number_period = 0
    birth_dead_number = 0
    card_childbirth = 0

    p_1 = 0
    p_3 = 0
    p_4 = 0
    p_5 = 0
    p_6 = 0
    p_7 = 0
    p_8 = 0
    p_9 = 0
    p_10 = 0
    p_11 = 0
    p_12 = 0
    p_13 = 0
    p_14 = 0
    p_15 = 0
    p_16 = 0
    p_17 = 0
    p_18 = 0
    p_19 = 0
    p_20 = 0
    p_25_1 = 0
    p_25_2 = 0
    p_26_1 = 0
    p_26_2 = 0
    p_27 = {
        'to_14': 0,
        '15_17': 0,
        '18_34': 0,
        '18_24': 0,
        '25_29': 0,
        '30_34': 0,
        '35_44': 0,
        '35_39': 0,
        '40_44': 0,
        '45_49': 0,
        '50_up': 0,
    }
    p_28 = 0
    p_29 = 0
    p_31  = {
        '22_23': 0,
        '24_27': 0,
        '24_25': 0,
        '26_27': 0,
        '28_36': 0,
        '28_30': 0,
        '31_33': 0,
        '34_36': 0,
        '37_41': 0,
        '42_up': 0,
    }
    
    if request.method == 'POST':
        form = StatisticsPeriodForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            if form_data['date_to'] - form_data['date_from'] < timedelta(days=0):
                form_data['date_from'], form_data['date_to'] = form_data['date_to'], form_data['date_from']

    for p in patients:
        card = p.card

        if card.age and 15 <= card.age <= 45:
            age_15_45 += 1

        if card.age and card.age < 18:
            age_less_18 += 1

        first_exam_list = p.first_examination.all()
        if len([x for x in first_exam_list]) >= 1:
            if first_exam_list[0].gestation_period_weeks and int(first_exam_list[0].gestation_period_weeks) < 12:
                p_1 += 1

        pregnancy_outcome_list = [x for x in p.pregnancy_outcome.all()]
        if any(x.pregnancy_outcome == 'a' for x in pregnancy_outcome_list) and card.age and 15 <= card.age <= 45:
            p_3 += len([x.pregnancy_outcome == 'a' for x in pregnancy_outcome_list])

        if any(x.pregnancy_outcome == 'd' for x in p.pregnancy_outcome.all()):
            p_12 += len([x.pregnancy_outcome == 'd' for x in pregnancy_outcome_list])
            birth_dead_number = p_12
            p_13 += len([(x.pregnancy_outcome == 'd' and x.gestation_period_weeks >= 28) for x in pregnancy_outcome_list])

        if any(x.pregnancy_outcome == 'b' for x in p.pregnancy_outcome.all()):
            birth_number += len([x.pregnancy_outcome == 'b' for x in pregnancy_outcome_list])
            if request.method == 'POST':
                for i in pregnancy_outcome_list:
                    if i.childbirth_date and form_data['date_from'] <= i.childbirth_date <= form_data['date_to']:
                        birth_number_period +=len([x.pregnancy_outcome == 'b' for x in pregnancy_outcome_list])

            p_15 += len([x.if_childbirth == 'ocs' for x in pregnancy_outcome_list])
            if card.age:
                if card.age < 18:
                    p_8 += 1
                if card.age >= 35:
                    p_7 += 1

        if any((x.imt if x.imt else 0) >= 30 for x in p.patient_information.all()):
            p_9 += 1
        
        if card.gestation_period_weeks and card.gestation_period_weeks < 12:
            p_11 += 1
        
        pregnancy_info_list = [x for x in p.pregnancy_info.all()]
        if len(pregnancy_info_list) == 1 and pregnancy_info_list[0].pregnancy == '1':
            p_10 += 1
            if request.method == 'POST':
                if form_data['date_from'] <= pregnancy_info_list[0].last_menstruation <= form_data['date_to']:
                    if any(x.pregnancy_1 == '1' for x in pregnancy_info_list) and any(x.presentation == '1' for x in p.uzi_exam_2.all()):
                        p_18 += 1
            else:
                if any(x.pregnancy_1 == '1' for x in pregnancy_info_list) and any(x.presentation == '1' for x in p.uzi_exam_2.all()):
                    p_18 += 1
        
        if any(x.pregnancy == '4' for x in pregnancy_info_list):
            p_6 += len([x.pregnancy == '4' for x in pregnancy_info_list])
        
        if any(x.pregnancy_1 == '2' for x in pregnancy_info_list):
            p_14 += len([x.pregnancy_1 == '2' for x in pregnancy_info_list])
        
        if request.method == 'POST':
            if pregnancy_info_list and pregnancy_info_list[0].last_menstruation and form_data['date_from'] <= pregnancy_info_list[0].last_menstruation <= form_data['date_to']:
                if len(pregnancy_info_list) >= 2 and any(x.if_childbirth == 'ocs' for x in pregnancy_outcome_list) \
                        and any(x.pregnancy_1 == '1' for x in pregnancy_info_list) and any(x.presentation == '1' for x in p.uzi_exam_2.all()):
                    p_19 += len([x.if_childbirth == 'ocs' for x in pregnancy_outcome_list])
            if card.childbirth_date and form_data['date_from'] <= card.childbirth_date <= form_data['date_to']:
                if card.diagnosis and 'O14.1' in card.diagnosis:
                    p_16 += 1

                if card.diagnosis and 'O15' in card.diagnosis:
                    p_20 += 1
        else:
            if len(pregnancy_info_list) >= 2 and any(x.if_childbirth == 'ocs' for x in pregnancy_outcome_list) \
                    and any(x.pregnancy_1 == '1' for x in pregnancy_info_list) and any(x.presentation == '1' for x in p.uzi_exam_2.all()):
                p_19 += len([x.if_childbirth == 'ocs' for x in pregnancy_outcome_list])
            
            if card.diagnosis and 'O14.1' in card.diagnosis:
                p_16 += 1

            if card.diagnosis and 'O15' in card.diagnosis:
                p_20 += 1

        normal_pregnancy = [
            'Z32.1', 'Z33', 'Z34.0', 'Z34.8', 'Z35.0', 'Z35.1', 'Z35.2',
            'Z35.3', 'Z35.4', 'Z35.5', 'Z35.6', 'Z35.7', 'Z35.8', 'Z35.9',
            'Z36.0', 'Z36.3'
            ]
        pathology_pregnancy = [
            'O10', 'O11', 'O12', 'O13', 'O14', 'O15', 'O16', 'O20',
            'O21', 'O22', 'O23', 'O24', 'O25', 'O26', 'O27', 'O28',
            'O29', 'O30', 'O31', 'O32', 'O33', 'O34', 'O35', 'O36',
            'O37', 'O38', 'O39', 'O40', 'O41', 'O42', 'O43', 'O44',
            'O45', 'O46', 'O47', 'O48', 'O98', 'O99'
            ]

        if request.method == 'POST':
            if card.childbirth_date and form_data['date_from'] <= card.childbirth_date <= form_data['date_to']:
                if any(x in (card.diagnosis if card.diagnosis else '') for x in normal_pregnancy):
                    p_25_1 += 1
                if any(x in (card.diagnosis if card.diagnosis else '') for x in pathology_pregnancy):
                    p_25_2 += 1

                if card.diagnosis and 'O80' in card.diagnosis:
                    p_26_1 += 1
                if any(x in (card.diagnosis if card.diagnosis else '') for x in ['O81', 'O82', 'O83', 'O84']):
                    p_26_2 += 1
            
            for i in [x.childbirth_date for x in pregnancy_outcome_list]:
                if card.age and i and (form_data['date_from'] <= i.date() <= form_data['date_to']):
                    if card.age <= 14:
                        p_27['to_14'] += 1
                    elif 15 <= card.age <= 17:
                        p_27['15_17'] += 1
                    elif 18 <= card.age <= 24:
                        p_27['18_24'] += 1
                        p_27['18_34'] += 1
                    elif 25 <= card.age <= 29:
                        p_27['25_29'] += 1
                        p_27['18_34'] += 1
                    elif 30 <= card.age <= 34:
                        p_27['30_34'] += 1
                        p_27['35_44'] += 1
                    elif 35 <= card.age <= 39:
                        p_27['35_39'] += 1
                        p_27['35_44'] += 1
                    elif 40 <= card.age <= 44:
                        p_27['40_44'] += 1
                        p_27['35_44'] += 1
                    elif 45 <= card.age <= 49:
                        p_27['45_49'] += 1
                    elif 50 <= card.age:
                        p_27['50_up'] += 1
                    break
        else:
            if any(x in (card.diagnosis if card.diagnosis else '') for x in normal_pregnancy):
                p_25_1 += 1
            if any(x in (card.diagnosis if card.diagnosis else '') for x in pathology_pregnancy):
                p_25_2 += 1

            if card.diagnosis and 'O80' in card.diagnosis:
                p_26_1 += 1
            if any(x in (card.diagnosis if card.diagnosis else '') for x in ['O81', 'O82', 'O83', 'O84']):
                p_26_2 += 1

            if any(x.childbirth_date for x in pregnancy_outcome_list) and card.age:
                if card.age <= 14:
                    p_27['to_14'] += 1
                elif 15 <= card.age <= 17:
                    p_27['15_17'] += 1
                elif 18 <= card.age <= 24:
                    p_27['18_24'] += 1
                    p_27['18_34'] += 1
                elif 25 <= card.age <= 29:
                    p_27['25_29'] += 1
                    p_27['18_34'] += 1
                elif 30 <= card.age <= 34:
                    p_27['30_34'] += 1
                    p_27['35_44'] += 1
                elif 35 <= card.age <= 39:
                    p_27['35_39'] += 1
                    p_27['35_44'] += 1
                elif 40 <= card.age <= 44:
                    p_27['40_44'] += 1
                    p_27['35_44'] += 1
                elif 45 <= card.age <= 49:
                    p_27['45_49'] += 1
                elif 50 <= card.age:
                    p_27['50_up'] += 1
    
        if card.diagnosis:
            p_28 += 1
        if card.diagnosis or any(x for x in pregnancy_outcome_list):
            p_29 += 1
        
        if request.method == 'POST':
            if card.childbirth_date and form_data['date_from'] <= card.childbirth_date <= form_data['date_to']:
                if card.childbirth_gestation_period:
                    card_childbirth += 1
                    if 22 <= card.childbirth_gestation_period <= 23:
                        p_31['22_23'] += 1
                    if 24 <= card.childbirth_gestation_period <= 25:
                        p_31['24_25'] += 1
                        p_31['24_27'] += 1
                    if 26 <= card.childbirth_gestation_period <= 27:
                        p_31['26_27'] += 1
                        p_31['24_27'] += 1
                    if 28 <= card.childbirth_gestation_period <= 30:
                        p_31['28_30'] += 1
                        p_31['28_36'] += 1
                    if 31 <= card.childbirth_gestation_period <= 33:
                        p_31['31_33'] += 1
                        p_31['28_36'] += 1
                    if 34 <= card.childbirth_gestation_period <= 36:
                        p_31['34_36'] += 1
                        p_31['28_36'] += 1
                    if 37 <= card.childbirth_gestation_period <= 41:
                        p_31['37_41'] += 1
                    if card.childbirth_gestation_period >= 42:
                        p_31['42_up'] += 1
        else:
            if card.childbirth_gestation_period:
                card_childbirth += 1
                if 22 <= card.childbirth_gestation_period <= 23:
                    p_31['22_23'] += 1
                if 24 <= card.childbirth_gestation_period <= 25:
                    p_31['24_25'] += 1
                    p_31['24_27'] += 1
                if 26 <= card.childbirth_gestation_period <= 27:
                    p_31['26_27'] += 1
                    p_31['24_27'] += 1
                if 28 <= card.childbirth_gestation_period <= 30:
                    p_31['28_30'] += 1
                    p_31['28_36'] += 1
                if 31 <= card.childbirth_gestation_period <= 33:
                    p_31['31_33'] += 1
                    p_31['28_36'] += 1
                if 34 <= card.childbirth_gestation_period <= 36:
                    p_31['34_36'] += 1
                    p_31['28_36'] += 1
                if 37 <= card.childbirth_gestation_period <= 41:
                    p_31['37_41'] += 1
                if card.childbirth_gestation_period >= 42:
                    p_31['42_up'] += 1

    if not birth_number:
        birth_number = 1
    if not birth_number_period:
        birth_number_period = 1
    if not birth_dead_number:
        birth_dead_number = 1
        
    if not request.method == 'POST':
        birth_number_period = birth_number
    return render(request, template_name, {
        'form': form,
        'p_1': p_1*100/patients_number,
        'p_3': p_3*1000/age_15_45,
        # 'p_4': p_3,
        # 'p_5': p_3,
        'p_6': p_6*100/birth_number,
        'p_7': p_7*100/birth_number,
        'p_8': p_8*100/birth_number,
        'p_9': p_9*100/birth_number,
        'p_10': p_10*100/birth_number,
        'p_11': p_11*100/birth_number,
        'p_12': p_12*1000/(birth_number + birth_dead_number),
        'p_13': p_13*1000/(birth_number + birth_dead_number),
        'p_14': p_14*100/birth_number,
        'p_15': p_15*100/birth_number,
        'p_16': p_16*1000/birth_number_period,
        # 'p_17': p_17,
        'p_18': p_18*100/birth_number_period,
        'p_19': p_19*100/birth_number_period,
        'p_20': p_20*100/birth_number_period,
        'p_21': p_6*1000/birth_number_period, ###
        'p_25': {
                '1': p_25_1*100/birth_number_period,
                '2': p_25_2*100/birth_number_period
                },
        'p_26': {
                '1': p_26_1*100/birth_number_period,
                '2': p_26_2*100/birth_number_period
                },
        'p_27': {x: p_27[x]*100/birth_number_period for x in p_27},
        'p_28': p_28*100/patients_number,
        'p_29': p_29*100/patients_number,
        'p_31': {x: p_31[x]*100/birth_number_period for x in p_31},
        'ex' : {'abc': 5, 'zxc': 10}
    })


def samd_page(request: HttpRequest, profile_id: int) -> HttpResponse:
    template_name: str = 'users/samd.html'
    return render(request, template_name, { 'profile_id': profile_id })

samd_temlates = {
    'medical_services_provision_referral': medical_services_provision_referral,
    'instrumental_research_protocol': instrumental_research_protocol,
    'laboratory_test_protocol': laboratory_test_protocol,
    'patient_examination_consultation': patient_examination_consultation,
    'treatment_in_hospital': treatment_in_hospital,
    'maternity_hospital_discharge_epicrisis': maternity_hospital_discharge_epicrisis,
    'cytological_examination_protocol': cytological_examination_protocol,
    'medical_death_certificate': medical_death_certificate,
    'medical_perinatal_death_certificate': medical_perinatal_death_certificate,
}

def generate_samd_page(request: HttpRequest, profile_id: int, samd: str) -> HttpResponse:
    template_name: str = 'users/generate_samd.html'
    print(f'{samd_temlates[samd]()}')
    return HttpResponseRedirect(reverse('samd', kwargs={ 'profile_id': profile_id }))

