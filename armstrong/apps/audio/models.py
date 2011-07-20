from django.db import models

from armstrong.apps.content.models import Content
from armstrong.core.arm_content.mixins import AudioMixin


class Audio(Content, AudioMixin): pass;
