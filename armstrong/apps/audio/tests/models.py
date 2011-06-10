import random
from datetime import datetime, time, timedelta
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings
from ._utils import generate_random_event, TestCase, hours_ago, hours_ahead, \
        end_of_day, start_of_day
from ..models import Event


class AudioPublicationTestCase(TestCase):

    def test_get_absolute_url(self):
        event = generate_random_event(hours_ago(1), hours_ahead(1))
        self.assertEqual(event.get_absolute_url(), '/%s/' % event.slug)

    def test_event_all_day_save(self):
        event = generate_random_event(hours_ago(1), hours_ahead(1))
        event.all_day = True
        event.save()

        self.assertEqual(event.start_date, start_of_day())
        self.assertEqual(event.end_date, end_of_day())

    def test_event_in_progress(self):
        event = generate_random_event(hours_ago(1), hours_ahead(1))
        self.assertFalse(event.has_passed)

    def test_event_passed(self):
        event = generate_random_event(hours_ago(2), hours_ago(1))
        self.assertTrue(event.has_passed)
