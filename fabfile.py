from armstrong.dev.tasks import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.arm_content',
        'armstrong.apps.audio',
        'armstrong.core.arm_sections',
        'south',
    ),
    'SITE_ID': 1,
}

main_app = "audio"
tested_apps = (main_app, )
