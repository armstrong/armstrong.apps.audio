from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from armstrong.core.arm_content.mixins import PublicationMixin, AuthorsMixin

from armstrong.core.arm_content.fields import AudioField

class AudioPublication(PublicationMixin, AuthorsMixin):
    file=AudioField()
    playtime=models.PositiveIntegerField("playtime in seconds",null=True, blank=True)    
    filetype=models.CharField("filetype",null=True, blank=True)    


    def save(*args, **kwargs):
        if hasattr(self.file, metadata):
            #populate stuff
            if 

