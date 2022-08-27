from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # felds = '__all__'
        fields = ('username', 'fio', 'gender', 'date_of_birth', 'groups')
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'gender', 'date_of_birth', 'groups')