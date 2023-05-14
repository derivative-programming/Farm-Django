from django.test import TestCase
from api.models import Role 
from api.models.factories.Role import RoleFactory


class RoleTestCase(TestCase):
    def setUp(self): 
        self.role = RoleFactory.create()

    def test_role_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.role)

    def test_role_fields(self): 
        self.assertIsInstance(self.role, Role)
        self.assertIsNotNone(self.role.code)
        self.assertIsNotNone(self.role.insert_user_id)
        self.assertIsNotNone(self.role.last_update_user_id)
        self.assertIsNotNone(self.role.description)
        self.assertIsNotNone(self.role.display_order)
        self.assertIsNotNone(self.role.is_active)
        self.assertIsNotNone(self.role.lookup_enum_name)
        self.assertIsNotNone(self.role.name)
        self.assertIsNotNone(self.role.pac)