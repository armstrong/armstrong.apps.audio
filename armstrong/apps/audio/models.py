from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from armstrong.core.arm_content.models import ContentBase

from armstrong.core.arm_content.fields import AudioField


class AudioPublication(ContentBase):
    file = AudioField(upload_to='audio/')
    playtime = models.PositiveIntegerField("playtime in seconds",
                                           null=True,
                                           blank=True)

    filetype = models.CharField("filetype",
                                max_length=16,
                                null=True,
                                blank=True)

    artist = models.CharField("artist",
                              max_length=100,
                              null=True,
                              blank=True,
                             )

    genre = models.CharField("genre",
                              max_length=100,
                              null=True,
                              blank=True,
                             )

    def save(self, *args, **kwargs):
        if hasattr(self.file, metadata):
            #populate stuff
            pass
