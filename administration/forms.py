from django import forms
from .models import Files


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'description', 'document']
        widgets = {
            'document': forms.FileInput(attrs={'required': False,'class': 'form-control'})
        }