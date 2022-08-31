from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from .models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        del self.fields['password1']
        del self.fields['password2']
    
    class Meta:
        model = CustomUser
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
        widgets = {
            'date_of_birth': DateInput(),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'