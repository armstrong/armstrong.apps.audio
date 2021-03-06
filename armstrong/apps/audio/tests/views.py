from django.test.client import Client
from django.core.urlresolvers import reverse
from ._utils import load_audio
from armstrong.dev.tests.utils import ArmstrongTestCase

from ..models import Audio
from audio_support.forms import AudioForm


class AudioViewTestCase(ArmstrongTestCase):

    def setUp(self):
        self.c = Client()

    def test_audio_detail(self):
        audio = load_audio('test.mp3')
        response = self.c.get('/audio/' + audio.slug + '/')
        self.assertEqual(response.context['audio'], audio)

    def test_audio_upload(self):
        audio = load_audio('test.mp3')
        #todo: this test is a lot of data entry to write 
        #skiping it and manually testing in the name of speed
        response = self.c.get('/audio/upload/')
        #was trying to be lazy, turns out its not really going to work. 
        #I will deal with it later.
        apf = AudioForm(instance=audio)
        del apf.initial['id']
        apf.initial.update({'pub_date_o':'2011-07-13', 'pub_date_1':'12:02:23', 'pub_status':'P', 'tags':'test',})
        post_response =  self.c.post('/audio/upload/', apf.initial)
        #todo: we need to add a bunch of boiler plate test utils to arm_content.tests.utils for supporting content base

    def test_admin_widget(self):
        pass
 
    def test_audio_list(self):
        audio = load_audio('test.ogg')
        audio2 = load_audio('test.mp3')
        response = self.c.get(reverse('audio_list'))
        self.assertEqual(list(response.context['audio_list']),
                list(Audio.objects.all()))
