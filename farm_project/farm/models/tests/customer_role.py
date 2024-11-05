# farm/models/tests/test_customer_role.py
from django.test import TestCase
from farm.models import CustomerRole
from farm.models.factories import CustomerRoleFactory
from farm.models import CurrentRuntime
class CustomerRoleTestCase(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.customer_role = CustomerRoleFactory.create()
    def test_customer_role_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.customer_role)
    def test_customer_role_fields(self):
        self.assertIsInstance(self.customer_role, CustomerRole)
        self.assertIsNotNone(self.customer_role.customer_role_id)
        self.assertIsNotNone(self.customer_role.code)
        self.assertIsNotNone(self.customer_role.insert_utc_date_time)
        self.assertIsNotNone(self.customer_role.last_update_utc_date_time)
        self.assertIsNotNone(self.customer_role.insert_user_id)
        self.assertIsNotNone(self.customer_role.last_update_user_id)
        self.assertIsNotNone(self.customer_role.last_change_code)
        self.assertIsNotNone(self.customer_role.customer) #customer_id
        self.assertIsNotNone(self.customer_role.is_placeholder)
        self.assertIsNotNone(self.customer_role.placeholder)
        self.assertIsNotNone(self.customer_role.role) #role_id
