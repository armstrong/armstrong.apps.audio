from django.views.generic.list import MultipleObjectMixin
from django.views.generic import  DetailView, CreateView, ListView

from .models import AudioPublication


class AudioPublicationList(ListView):
    model = AudioPublication


class AudioPublicationDetail(DetailView):
    model = AudioPublication


class AudioPublicationCreateView(CreateView):
    model = AudioPublication
