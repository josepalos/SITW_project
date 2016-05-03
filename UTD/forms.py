from django.forms import ModelForm
from models import Provider


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        exclude = ['album']
