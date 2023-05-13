from django.test import TestCase
from api.models import Customer 
from api.factories import CustomerFactory 



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
        customer = CustomerFactory.create()
        self.assertIsInstance(customer, Customer)
        self.assertIsNotNone(customer.customer_id)
        self.assertIsNotNone(customer.code)
        self.assertIsNotNone(customer.insert_utc_date_time)
        self.assertIsNotNone(customer.last_update_utc_date_time)
        self.assertIsNotNone(customer.first_name)
        self.assertIsNotNone(customer.last_name)
        self.assertIsNotNone(customer.email)
        self.assertIsNotNone(customer.password)
        self.assertIsNotNone(customer.phone)
        self.assertIsNotNone(customer.province)
        self.assertIsNotNone(customer.zip)
        self.assertIsNotNone(customer.tac)
        self.assertIsNotNone(customer.active_organization_id)
        self.assertIsNotNone(customer.last_change_code)