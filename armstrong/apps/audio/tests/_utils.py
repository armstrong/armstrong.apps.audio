from datetime import datetime, timedelta, date, time
import random

from django.test import TestCase as DjangoTestCase
from django.test.client import RequestFactory
from django.core.files import File

from ..models import Event

def load_audio_pub(filename):
    #todo: there needs to be a better way to get the filename
    f= open('./armstrong/apps/audio/tests/arm_audio_support/static/audio/' + filename,"rb+")
    uf=File(file=f)
    pub_date = datetime.now()
    pub_status = 'P'
    slug = 'random-slug-%s' % random.randint(100,1000)
    title = 'Random title %s' % random.randint(100,1000)
    am = AudioPublication(pub_date=pub_date, pub_status=pub_status, slug=slug, title=title, audio_file=uf)
    am.save()
    return am

class TestCase(DjangoTestCase):
    pass


