from .models import Patient, Doctor, MedicalHistory, SelfMonitoringRecords, ReceptionNotes, MedicalCard
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from .choices import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class PatientCreationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'gender',
            'telephone',
            'email',
        )
        # widgets = {
        #     'date_of_birth': DateInput(),
        #     'date_death': DateInput(),
        # }


class DoctorCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'cabinet',
        )


class PatientChangeForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'gender',
            'telephone',
            'email',
        )


class DiseaseCreationForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = (
            'disease',
            'date_cured',
        )
        widgets = {
            'date_cured': DateInput(),
        }


class RecordCreationForm(forms.ModelForm):
    class Meta:
        model = SelfMonitoringRecords
        fields = (
            'title',
            'description',
        )


class PatientFilterForm(forms.Form):
    CHOICES = (
            ('d', 'Текущий день'),
            ('w', 'Текущая неделя'),
            ('m', 'Текущий месяц'),
            ('30', '30 дней'),
        )
    time_interval = forms.ChoiceField(label='Временной промежуток', choices=CHOICES)
    territory = forms.BooleanField(label='Мои территории', required=False)


class ReceptionAddForm(forms.ModelForm):
    class Meta:
        model = ReceptionNotes
        fields = (
            'med_organization', 'cabinet', 'date_meeting',
        )
        widgets = {
            'date_meeting': DateTimeInput()
        }


class DataSamplingForm(forms.Form):    
    mkb_10 = forms.CharField(label='Заболевание по МКБ-10', max_length=270, required=False)
    medical_organization = forms.ChoiceField(label='Медицинская организация', choices=MEDICAL_ORGANIZATION, required=False)
    territory = forms.ChoiceField(label='Территория', choices=TERRITORY, required=False)
    gender = forms.ChoiceField(label='Пол', choices=GENDERS, required=False)
    age = forms.IntegerField(label='Возраст', validators=[MinValueValidator(1), MaxValueValidator(100)], required=False)
    date_of_birth = forms.DateField(label='Дата рождения', required=False, widget=DateInput())
    date_of_death = forms.DateTimeField(label='Дата смерти', required=False, widget=DateTimeInput())
    city_village = forms.ChoiceField(label='Житель города/села', choices=CITYVILLAGE, required=False)


class MedicalCardForm(forms.ModelForm):
    class Meta:
        model = MedicalCard
        fields = 'date_of_birth', 'residence_address', 'registration_address', \
        'mobile_phone', 'home_phone', 'work_phone', 'email', 'marital_status', \
        'trusted_person_fio', 'trusted_person_phone', 'oms_policy', 'snils', 'maternity_leave_start', \
        'maternity_leave_finish', 'disability_certificate', 'generic_certificate_number', \
        'generic_certificate_date', 'allergy', 'allergy_description', 'pregnancy_count', \
        'gestation_period_weeks', 'first_visit_date', 'childbirth_date', 'childbirth_gestation_period', \
        'med_org', 'diagnosis', 'complications', 'somatic_diseases', 'gynecological_diseases', 'doctor_confirmation'
        widgets = {
            'date_of_birth': DateInput(),
            'maternity_leave_start': DateInput(),
            'maternity_leave_finish': DateInput(),
            'generic_certificate_date': DateInput(),
            'first_visit_date': DateInput(),
            'childbirth_date': DateInput()
        }
