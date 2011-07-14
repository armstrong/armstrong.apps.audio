from django.views.generic.list import MultipleObjectMixin
from django.views.generic import  DetailView, CreateView, ListView

from .models import Audio


class ListView(ListView):
    context_object_name = "audio_publication_list"
    model = Audio


class DetailView(DetailView):
    context_object_name = "audio_publication"
    model = Audio


class CreateView(CreateView):
    model = Audio
