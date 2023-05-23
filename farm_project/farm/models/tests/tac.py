# farm/models/tests/test_tac.py
from django.test import TestCase
from farm.models import Tac
from farm.models.factories import TacFactory
class TacTestCase(TestCase):
    def setUp(self): 
        self.tac = TacFactory.create()
    def test_tac_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.tac)
    def test_tac_fields(self): 
        self.assertIsInstance(self.tac, Tac)
        self.assertIsNotNone(self.tac.tac_id)
        self.assertIsNotNone(self.tac.code)
        self.assertIsNotNone(self.tac.insert_utc_date_time)
        self.assertIsNotNone(self.tac.last_update_utc_date_time)
        self.assertIsNotNone(self.tac.insert_user_id)
        self.assertIsNotNone(self.tac.last_update_user_id)
        self.assertIsNotNone(self.tac.last_change_code)
        self.assertIsNotNone(self.tac.description)
        self.assertIsNotNone(self.tac.display_order)
        self.assertIsNotNone(self.tac.is_active)
        self.assertIsNotNone(self.tac.lookup_enum_name)
        self.assertIsNotNone(self.tac.name)
        self.assertIsNotNone(self.tac.pac) #pac_id
