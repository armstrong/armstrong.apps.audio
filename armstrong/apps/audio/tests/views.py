from datetime import date, timedelta
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from ._utils import load_audio_pub, TestCase

from ..models import AudioPublication
from audio_support.forms import AudioPubForm

class AudioViewTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_audio_detail(self):
        audio_pub = load_audio_pub('test.mp3')
        response = self.c.get( '/audio/' + audio_pub.slug+'/')
        self.assertEqual(response.context['audio_publication'], audio_pub)

    def test_audio_upload(self):
        audio_pub = load_audio_pub('test.mp3')
        #todo: this test is a lot of data entry to write skiping it and manually testing in the name of speed
        response = self.c.get('/audio/upload/')
        apf=AudioPubForm(instance=audio_pub)
        del apf.initial['id']
        apf.initial.update({'pub_date_o':'2011-07-13', 'pub_date_1':'12:02:23', 'pub_status':'P', 'tags':'test',})
        post_response =  self.c.post('/audio/upload/', apf.initial)
        #todo: we need to add a bunch of boiler plate test utils to arm_content.tests.utils for supporting content base

    def test_admin_widget(self):
        pass
 
    def test_audio_list(self):
        audio_pub = load_audio_pub('test.ogg')
        audio_pub2 = load_audio_pub('test.mp3')
        response = self.c.get(reverse('audio_list'))
        self.assertEqual(list(response.context['audio_publication_list']),
                list(AudioPublication.objects.all()))
