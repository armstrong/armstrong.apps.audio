from django import forms
from armstrong.apps.audio.models import Audio


class AudioForm(forms.ModelForm):
    class meta:
        model = Audio
