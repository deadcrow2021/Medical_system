from .models import Patient, Doctor, MedicalHistory, SelfMonitoringRecords, ReceptionNotes
from django import forms

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
            'date_of_birth',
            'gender',
            'social_status',
            'disability',
            'blood',
            'telephone',
            'work_address',
            'oms_policy',
            'insurance',
            'snils',
            'city_village',
            'address',
            'territory',
            'date_death'
        )
        widgets = {
            'date_of_birth': DateInput(),
            'date_death': DateInput(),
        }


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
            'date_of_birth',
            'gender',
            'social_status',
            'disability',
            'blood',
            'telephone',
            'work_address',
            'oms_policy',
            'insurance',
            'snils',
            'city_village',
            'address',
            'territory',
            'date_death'
        )
        widgets = {
            'date_death': DateInput(),
        }


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
            'date_meeting',
        )
        widgets = {
            'date_meeting': DateTimeInput()
        }