from django.test import TestCase
from api.models import Organization 
 



class OrganizationTestCase(TestCase):
    def test_organization(self):
        self.assertEquals(
            Organization.objects.count(),
            0
        )
        Organization.objects.create() 
        self.assertEquals(
            Organization.objects.count(),
            1
        ) 

# TODO