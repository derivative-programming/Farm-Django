from django.test import TestCase
from api.models import Customer 
 



class CustomerTestCase(TestCase):
    def test_customer(self):
        self.assertEquals(
            Customer.objects.count(),
            0
        )
        Customer.objects.create() 
        self.assertEquals(
            Customer.objects.count(),
            1
        ) 