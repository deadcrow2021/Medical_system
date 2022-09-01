from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from .models import Patient, Doctor

class DateInput(forms.DateInput):
    input_type = 'date'

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
            'territory'
        )
        widgets = {
            'date_of_birth': DateInput(),
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


class PatientChangeForm(UserChangeForm):
    class Meta:
        model = Patient
        fields = [
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
            'territory'
        ]
