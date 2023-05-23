# farm/models/tests/test_date_greater_than_filter.py
from django.test import TestCase
from farm.models import DateGreaterThanFilter
from farm.models.factories import DateGreaterThanFilterFactory
class DateGreaterThanFilterTestCase(TestCase):
    def setUp(self): 
        self.date_greater_than_filter = DateGreaterThanFilterFactory.create()
    def test_date_greater_than_filter_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.date_greater_than_filter)
    def test_date_greater_than_filter_fields(self): 
        self.assertIsInstance(self.date_greater_than_filter, DateGreaterThanFilter)
        self.assertIsNotNone(self.date_greater_than_filter.date_greater_than_filter_id)
        self.assertIsNotNone(self.date_greater_than_filter.code)
        self.assertIsNotNone(self.date_greater_than_filter.insert_utc_date_time)
        self.assertIsNotNone(self.date_greater_than_filter.last_update_utc_date_time)
        self.assertIsNotNone(self.date_greater_than_filter.insert_user_id)
        self.assertIsNotNone(self.date_greater_than_filter.last_update_user_id)
        self.assertIsNotNone(self.date_greater_than_filter.last_change_code)
        self.assertIsNotNone(self.date_greater_than_filter.day_count)
        self.assertIsNotNone(self.date_greater_than_filter.description)
        self.assertIsNotNone(self.date_greater_than_filter.display_order)
        self.assertIsNotNone(self.date_greater_than_filter.is_active)
        self.assertIsNotNone(self.date_greater_than_filter.lookup_enum_name)
        self.assertIsNotNone(self.date_greater_than_filter.name)
        self.assertIsNotNone(self.date_greater_than_filter.pac) #pac_id
