from django.forms import ModelForm
from models import Provider, Playlist
from django import forms

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        exclude = ['album']
        widgets = {
            'provider_name': forms.TextInput()
        }

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        exclude = ['user', 'songs', 'last_update']
        widgets = {
            'name': forms.TextInput()
        }