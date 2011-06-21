from django.views.generic import list_detail

from .models import AudioPublication


class AudioPublicationList(list_detail.object_list):
    model = AudioPublication


class AudioPublicationDetail(list_detail.object_detail):
    model = AudioPublication


class AudioPublicationCreateView(CreateView):
    model = AudioPublication
