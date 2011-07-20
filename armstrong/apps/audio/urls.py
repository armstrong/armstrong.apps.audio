from django.conf.urls.defaults import *
from armstrong.apps.audio import views as audio_views

urlpatterns = patterns('',

    url(r'^$', audio_views.ListView.as_view(),
                name='audio_list'),

    url(r'^upload/$', audio_views.CreateView.as_view(),
                name='audio_upload'),

    url(r'^(?P<slug>[-\w]+)/$', audio_views.DetailView.as_view(),
                name='audio_detail'),
)
