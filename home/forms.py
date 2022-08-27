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
        fields = ('username', 'fio', 'date_of_birth')
        widgets = {
            'date_of_birth': DateInput(),
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('groups')
        self.fields.pop('password1')
        self.fields.pop('password2')
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'gender', 'date_of_birth', 'groups')