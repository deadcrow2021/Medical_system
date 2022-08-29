from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from .models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields.pop('groups')

    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'date_of_birth')
        widgets = {
            'date_of_birth': DateInput(),
        }
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'gender', 'date_of_birth', 'groups')
