from django.forms import ModelForm
from models import Provider
from django import forms

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        exclude = ['album']
        widgets = {
            'provider_name': forms.TextInput()
        }