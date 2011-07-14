from django.db import models

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

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return "%s by %s authored by %s" % (self.file, self.artist, self.authors)

    @property
    def player_as_html(self):
        return self.file.render()
