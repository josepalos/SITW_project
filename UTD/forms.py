from django.forms import ModelForm
from models import Provider, Playlist, Artist
from django import forms


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        exclude = ['album', 'user']
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


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'spotify_id': forms.TextInput(attrs={'readonly':'readonly'}),
        }
