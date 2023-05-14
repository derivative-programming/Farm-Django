from django.test import TestCase
from api.models import DateGreaterThanFilter 
from api.models.factories.DateGreaterThanFilter import DateGreaterThanFilterFactory


class DateGreaterThanFilterTestCase(TestCase):
    def setUp(self): 
        self.date_greater_than_filter = DateGreaterThanFilterFactory.create()

    def test_date_greater_than_filter_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.date_greater_than_filter)

    def test_date_greater_than_filter_fields(self): 
        # create a DateGreaterThanFilter object with default attributes 
        # assert that the object was created successfully
        self.assertIsInstance(self.date_greater_than_filter, DateGreaterThanFilter)
        self.assertIsNotNone(self.date_greater_than_filter.code)
        self.assertIsNotNone(self.date_greater_than_filter.insert_user_id)
        self.assertIsNotNone(self.date_greater_than_filter.last_update_user_id)
        self.assertIsNotNone(self.date_greater_than_filter.description)
        self.assertIsNotNone(self.date_greater_than_filter.display_order)
        self.assertIsNotNone(self.date_greater_than_filter.is_active)
        self.assertIsNotNone(self.date_greater_than_filter.lookup_enum_name)
        self.assertIsNotNone(self.date_greater_than_filter.name)
        self.assertIsNotNone(self.date_greater_than_filter.pac)