# farm/models/tests/test_flavor.py
from django.test import TestCase
from farm.models import Flavor
from farm.models.factories import FlavorFactory
from farm.models import CurrentRuntime
class FlavorTestCase(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.flavor = FlavorFactory.create()
    def test_flavor_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.flavor)
    def test_flavor_fields(self):
        self.assertIsInstance(self.flavor, Flavor)
        self.assertIsNotNone(self.flavor.flavor_id)
        self.assertIsNotNone(self.flavor.code)
        self.assertIsNotNone(self.flavor.insert_utc_date_time)
        self.assertIsNotNone(self.flavor.last_update_utc_date_time)
        self.assertIsNotNone(self.flavor.insert_user_id)
        self.assertIsNotNone(self.flavor.last_update_user_id)
        self.assertIsNotNone(self.flavor.last_change_code)
        self.assertIsNotNone(self.flavor.description)
        self.assertIsNotNone(self.flavor.display_order)
        self.assertIsNotNone(self.flavor.is_active)
        self.assertIsNotNone(self.flavor.lookup_enum_name)
        self.assertIsNotNone(self.flavor.name)
        self.assertIsNotNone(self.flavor.pac) #pac_id
