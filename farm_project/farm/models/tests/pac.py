# api/models/tests/test_pac.py
from django.test import TestCase
from farm.models import Pac
from farm.models.factories import PacFactory
class PacTestCase(TestCase):
    def setUp(self): 
        self.pac = PacFactory.create()
    def test_pac_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.pac)
    def test_pac_fields(self): 
        self.assertIsInstance(self.pac, Pac)
        self.assertIsNotNone(self.pac.pac_id)
        self.assertIsNotNone(self.pac.code)
        self.assertIsNotNone(self.pac.insert_utc_date_time)
        self.assertIsNotNone(self.pac.last_update_utc_date_time)
        self.assertIsNotNone(self.pac.insert_user_id)
        self.assertIsNotNone(self.pac.last_update_user_id)
        self.assertIsNotNone(self.pac.last_change_code)
        self.assertIsNotNone(self.pac.description)
        self.assertIsNotNone(self.pac.display_order)
        self.assertIsNotNone(self.pac.is_active)
        self.assertIsNotNone(self.pac.lookup_enum_name)
        self.assertIsNotNone(self.pac.name)
