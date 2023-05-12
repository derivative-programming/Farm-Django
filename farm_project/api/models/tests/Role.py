from django.test import TestCase
from api.models import Role 
 



class RoleTestCase(TestCase):
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