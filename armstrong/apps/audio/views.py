from django.views.generic.list import MultipleObjectMixin
from django.views.generic import  DetailView, CreateView, ListView

from .models import AudioPublication


class AudioPublicationList(ListView):
    context_object_name = "audio_publication_list"
    model = AudioPublication


class AudioPublicationDetail(DetailView):
    context_object_name = "audio_publication"
    model = AudioPublication


class AudioPublicationCreateView(CreateView):
    model = AudioPublication
