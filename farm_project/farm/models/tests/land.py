# farm/models/tests/test_land.py
from django.test import TestCase
from farm.models import Land
from farm.models.factories import LandFactory
from farm.models import CurrentRuntime
class LandTestCase(TestCase):
    def setUp(self): 
        CurrentRuntime.initialize()
        self.land = LandFactory.create()
    def test_land_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.land)
    def test_land_fields(self): 
        self.assertIsInstance(self.land, Land)
        self.assertIsNotNone(self.land.land_id)
        self.assertIsNotNone(self.land.code)
        self.assertIsNotNone(self.land.insert_utc_date_time)
        self.assertIsNotNone(self.land.last_update_utc_date_time)
        self.assertIsNotNone(self.land.insert_user_id)
        self.assertIsNotNone(self.land.last_update_user_id)
        self.assertIsNotNone(self.land.last_change_code)
        self.assertIsNotNone(self.land.description)
        self.assertIsNotNone(self.land.display_order)
        self.assertIsNotNone(self.land.is_active)
        self.assertIsNotNone(self.land.lookup_enum_name)
        self.assertIsNotNone(self.land.name)
        self.assertIsNotNone(self.land.pac) #pac_id
