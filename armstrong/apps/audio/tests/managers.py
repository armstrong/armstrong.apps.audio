import random
from datetime import date, timedelta, datetime
from django.core.urlresolvers import reverse
from ._utils import generate_random_event, TestCase, hours_ago, hours_ahead
from ..models import Event


class EventManagerTestCase(TestCase):

    def test_upcoming_future(self):
        event_future = generate_random_event(hours_ahead(1), hours_ahead(2))
        self.assertTrue(event_future in Event.objects.upcoming())

    def test_upcoming_in_progress(self):
        event_inprogress = generate_random_event(hours_ago(1), hours_ahead(1))
        self.assertTrue(event_inprogress in Event.objects.upcoming())
        self.assertTrue(event_inprogress in Event.objects.upcoming(days=1))

    def test_upcoming_happened_today(self):
        """ don't run this at 12am! go to bed """
        event_happened_today = generate_random_event(hours_ago(2), hours_ago(1))
        self.assertTrue(event_happened_today in Event.objects.upcoming())
        self.assertTrue(event_happened_today in Event.objects.upcoming(days=0))
        self.assertTrue(event_happened_today in Event.objects.upcoming(days=1))

    def test_upcoming_happened_yesterday(self):
        event_happened_yesterday = generate_random_event(hours_ago(25),
                hours_ago(24))
        self.assertFalse(event_happened_yesterday in Event.objects.upcoming())
        self.assertFalse(event_happened_yesterday in Event.objects.upcoming(days=0))
        self.assertFalse(event_happened_yesterday in Event.objects.upcoming(days=1))

    def test_upcoming_tmrw(self):
        event_tmrw = generate_random_event(hours_ahead(24),
                hours_ahead(25))
        self.assertFalse(event_tmrw in Event.objects.upcoming(days=0))
        self.assertTrue(event_tmrw in Event.objects.upcoming(days=1))

    def test_upcoming_3_days(self):
        event_3_days = generate_random_event(hours_ahead(24*3),
                hours_ahead(24*3+1))
        self.assertTrue(event_3_days in Event.objects.upcoming(days=3))
        self.assertFalse(event_3_days in Event.objects.upcoming(days=2))

    def test_upcoming_asc_order(self):
        events = [generate_random_event(hours_ago(i), hours_ago(i+1))
                for i in random.sample(xrange(-48, 48), 10)]

        upcoming = list(Event.objects.upcoming())
        self.assertTrue(upcoming == sorted(upcoming, key=lambda e: e.start_date))

    def test_upcoming_no_site(self):
        event = generate_random_event(hours_ahead(1), hours_ahead(2))
        self.assertTrue(event in Event.on_site.upcoming())
        event.sites.clear()
        self.assertFalse(event in Event.on_site.upcoming())
