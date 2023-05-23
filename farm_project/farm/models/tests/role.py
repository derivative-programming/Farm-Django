# api/models/tests/test_role.py
from django.test import TestCase
from farm.models import Role
from farm.models.factories import RoleFactory
class RoleTestCase(TestCase):
    def setUp(self): 
        self.role = RoleFactory.create()
    def test_role_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.role)
    def test_role_fields(self): 
        self.assertIsInstance(self.role, Role)
        self.assertIsNotNone(self.role.role_id)
        self.assertIsNotNone(self.role.code)
        self.assertIsNotNone(self.role.insert_utc_date_time)
        self.assertIsNotNone(self.role.last_update_utc_date_time)
        self.assertIsNotNone(self.role.insert_user_id)
        self.assertIsNotNone(self.role.last_update_user_id)
        self.assertIsNotNone(self.role.last_change_code)
        self.assertIsNotNone(self.role.description)
        self.assertIsNotNone(self.role.display_order)
        self.assertIsNotNone(self.role.is_active)
        self.assertIsNotNone(self.role.lookup_enum_name)
        self.assertIsNotNone(self.role.name)
        self.assertIsNotNone(self.role.pac) #pac_id
