from django.test import TestCase
from api.models import CustomerRole 
 



class CustomerRoleTestCase(TestCase):
    def test_customer_role(self):
        self.assertEquals(
            CustomerRole.objects.count(),
            0
        )
        CustomerRole.objects.create() 
        self.assertEquals(
            CustomerRole.objects.count(),
            1
        ) 