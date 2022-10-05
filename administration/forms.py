from django import forms
from .models import Files


class FileUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Files
        fields = ['title', 'description', 'document']
        widgets = {
            'document': forms.FileInput(attrs={'required': False,'class': 'form-control'})
        }