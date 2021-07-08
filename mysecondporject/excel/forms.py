from django.forms import ModelForm, ClearableFileInput
from django import forms
from django.forms.widgets import Textarea
from .models import MyFiles

class MyFilesForm(ModelForm):
    class Meta:
        model = MyFiles
        fields = '__all__'
        widgets = {
            'file': ClearableFileInput(attrs={'class': 'form-control-file'}),
            
        }

class AcceptForm(forms.Form):
    aceept = forms.BooleanField(label='', help_text='Acepta terminos y condiciones  ')

