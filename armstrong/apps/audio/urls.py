from django.conf.urls.defaults import *
from armstrong.apps.audio import views as AudioViews

urlpatterns = patterns('',

    url(r'^$', AudioViews.AudioPublicationList.as_view(),
                name='audio_list'),

    url(r'^upload/$', AudioViews.AudioPublicationCreateView.as_view(),
                name='audio_upload'),

    url(r'^(?P<slug>[-\w]+)/$', AudioViews.AudioPublicationDetail.as_view(),
                name='audio_detail'),

)
