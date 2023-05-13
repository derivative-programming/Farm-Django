from django.test import TestCase
from api.models import DateGreaterThanFilter 
from api.models.factories.DateGreaterThanFilter import DateGreaterThanFilterFactory


class DateGreaterThanFilterTestCase(TestCase):
    def setUp(self):
        DateGreaterThanFilter.objects.all().delete()

    def test_dateGreaterThanFilter(self):
        self.assertEquals(
            DateGreaterThanFilter.objects.count(),
            0
        )
        DateGreaterThanFilter.objects.create() 
        self.assertEquals(
            DateGreaterThanFilter.objects.count(),
            1
        )
        # create a DateGreaterThanFilter object with default attributes
        dateGreaterThanFilter = DateGreaterThanFilterFactory.create()
        # assert that the object was created successfully
        self.assertIsInstance(dateGreaterThanFilter, DateGreaterThanFilter)
        self.assertIsNotNone(dateGreaterThanFilter.code)
        self.assertIsNotNone(dateGreaterThanFilter.insert_user_id)
        self.assertIsNotNone(dateGreaterThanFilter.last_update_user_id)
        self.assertIsNotNone(dateGreaterThanFilter.description)
        self.assertIsNotNone(dateGreaterThanFilter.display_order)
        self.assertIsNotNone(dateGreaterThanFilter.is_active)
        self.assertIsNotNone(dateGreaterThanFilter.lookup_enum_name)
        self.assertIsNotNone(dateGreaterThanFilter.name)
        self.assertIsNotNone(dateGreaterThanFilter.pac)