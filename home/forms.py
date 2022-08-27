from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from .models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'
    
class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'gender', 'date_of_birth', 'groups')
        widgets = {
            'date_of_birth': DateInput(),
        }
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'gender', 'date_of_birth', 'groups')