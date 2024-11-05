# farm/models/tests/test_org_customer.py
from django.test import TestCase
from farm.models import OrgCustomer
from farm.models.factories import OrgCustomerFactory
from farm.models import CurrentRuntime
class OrgCustomerTestCase(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.org_customer = OrgCustomerFactory.create()
    def test_org_customer_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.org_customer)
    def test_org_customer_fields(self):
        self.assertIsInstance(self.org_customer, OrgCustomer)
        self.assertIsNotNone(self.org_customer.org_customer_id)
        self.assertIsNotNone(self.org_customer.code)
        self.assertIsNotNone(self.org_customer.insert_utc_date_time)
        self.assertIsNotNone(self.org_customer.last_update_utc_date_time)
        self.assertIsNotNone(self.org_customer.insert_user_id)
        self.assertIsNotNone(self.org_customer.last_update_user_id)
        self.assertIsNotNone(self.org_customer.last_change_code)
        self.assertIsNotNone(self.org_customer.customer) #customer_id
        self.assertIsNotNone(self.org_customer.email)
        self.assertIsNotNone(self.org_customer.organization) #organization_id
