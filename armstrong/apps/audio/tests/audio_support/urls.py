
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from armstrong.apps.audio import urls as AudioUrls

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^audio/', include(AudioUrls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)

