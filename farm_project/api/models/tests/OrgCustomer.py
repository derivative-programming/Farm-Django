from django.test import TestCase
from api.models import OrgCustomer 
 



class OrgCustomerTestCase(TestCase):
    def test_org_customer(self):
        self.assertEquals(
            OrgCustomer.objects.count(),
            0
        )
        OrgCustomer.objects.create() 
        self.assertEquals(
            OrgCustomer.objects.count(),
            1
        ) 