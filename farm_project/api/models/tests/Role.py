from django.test import TestCase
from api.models import Role 
from api.models.factories.Role import RoleFactory


class RoleTestCase(TestCase):
    def setUp(self):
        Role.objects.all().delete()

    def test_role(self):
        self.assertEquals(
            Role.objects.count(),
            0
        )
        Role.objects.create() 
        self.assertEquals(
            Role.objects.count(),
            1
        )
        # create a Role object with default attributes
        role = RoleFactory.create()
        # assert that the object was created successfully
        self.assertIsInstance(role, Role)
        self.assertIsNotNone(role.code)
        self.assertIsNotNone(role.insert_user_id)
        self.assertIsNotNone(role.last_update_user_id)
        self.assertIsNotNone(role.description)
        self.assertIsNotNone(role.display_order)
        self.assertIsNotNone(role.is_active)
        self.assertIsNotNone(role.lookup_enum_name)
        self.assertIsNotNone(role.name)
        self.assertIsNotNone(role.pac)