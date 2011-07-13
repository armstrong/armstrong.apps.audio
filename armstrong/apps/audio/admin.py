from django.contrib import admin
from django.conf import settings

from armstrong.core.arm_content.fields.widgets import AudioFileWidget
from armstrong.core.arm_content.fields import AudioField

from .models import *


class AudioPubAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AudioField: {'widget': AudioFileWidget},
    }

    class Media:
        css = {
                "all": (settings.STATIC_URL + "skin/jplayer.blue.monday.css",)
        }
        js = ("https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js",
            settings.STATIC_URL + "js/jquery.jplayer.min.js"
        )


admin.site.register(AudioPublication, AudioPubAdmin)
