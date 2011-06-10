from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from armstrong.core.arm_content.mixins.publication import PublicationMixin
from .fields import AudioField

class AudioPublication(PublicationMixin,AuthorMixin):
    file=AudioField()
    
    
