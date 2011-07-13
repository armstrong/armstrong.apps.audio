from datetime import date, timedelta
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from ._utils import load_audio_pub, TestCase
from ._utils import load_audio_pub, TestCase


class AudioViewTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_audio_detail(self):
        audio_pub = load_audio_pub('test.mp3')
        response = self.c.get(reverse('audio_detail') + '/' + audio_pub.title)
        self.assertEqual(response.context['audio_pub'], audio_pub)
        self.assertContains("stuff that it should contain")

    def test_audio_upload(self):
        pass 
    
    def test_admin_widget(self):
        pass
 
    def test_audio_list(self):
        audio_pub = load_audio_pub('test.ogg')
        audio_pub2 = load_audio_pub('test.mp3')
        response = self.c.get(reverse('audio_list'))
        self.assertEqual(list(response.context['audio_list']),
                list(AudioPublications.objects.all()))
