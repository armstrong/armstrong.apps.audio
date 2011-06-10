from datetime import date, timedelta
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from ._utils import load_audio_pub, TestCase


class AudioViewTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_audio_detail(self):
        audio_pub= load_audio_pub('test.mp3')
        response = self.c.get(audio_pub.get_absolute_url())
        self.assertEqual(response.context['audio_pub'], audio_pub)
        self.assertContains( "stuff that it should contain")

    def test_audio_type_unsupported(self):
        '''if the player cant play the file, it should render as a download link'''
        audio_pub = load_audio_pub('test.flac')
        response = self.c.get(audio_pub.get_absolute_url())
        self.assertContains(response, "href=\"%s\"" % audio_pub.file.url())

    def test_audio_list(self):
        audio_pub = load_audio_pub('test.flac')
        audio_pub2 = load_audio_pub('test.mp3')
        response = self.c.get(reverse('audio_pub_list'))

        self.assertEqual(list(response.context['audio_pub_list']),
                list(AudioPublications.objects.all()))
                
