from armstrong.dev.tasks import *

full_name= 'armstrong.apps.audio'
main_app = "audio"
tested_apps = (main_app, )

settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'taggit',
        'reversion',
        'armstrong.core.arm_content',
        'armstrong.core.arm_sections',
        'armstrong.apps.audio.tests.audio_support',
        'armstrong.apps.content',
        full_name,
        'south',
    ),
    'SITE_ID': 1,
    'ARMSTRONG_EXTERNAL_AUDIO_METADATA_BACKEND': 'armstrong.apps.audio.backends.id3reader.Id3readerBackend',
    'STATIC_ROOT': './armstrong/apps/audio/tests/audio_support/static/',
    'STATIC_URL': '/static/',
    'MEDIA_ROOT': './media/',
    'MEDIA_URL': '/media/',
    'ROOT_URLCONF': 'armstrong.apps.audio.tests.audio_support.urls',
}

