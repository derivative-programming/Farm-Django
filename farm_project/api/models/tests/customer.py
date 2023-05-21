# api/models/tests/test_customer.py
from django.test import TestCase
from api.models import Customer
from api.models.factories import CustomerFactory
class CustomerTestCase(TestCase):
    def setUp(self): 
        self.customer = CustomerFactory.create()
    def test_customer_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.customer)
    def test_customer_fields(self): 
        self.assertIsInstance(self.customer, Customer)
        self.assertIsNotNone(self.customer.customer_id)
        self.assertIsNotNone(self.customer.code)
        self.assertIsNotNone(self.customer.insert_utc_date_time)
        self.assertIsNotNone(self.customer.last_update_utc_date_time)
        self.assertIsNotNone(self.customer.insert_user_id)
        self.assertIsNotNone(self.customer.last_update_user_id)
        self.assertIsNotNone(self.customer.last_change_code)
        self.assertIsNotNone(self.customer.active_organization_id)
        self.assertIsNotNone(self.customer.email)
        self.assertIsNotNone(self.customer.email_confirmed_utc_date_time)
        self.assertIsNotNone(self.customer.first_name)
        self.assertIsNotNone(self.customer.forgot_password_key_expiration_utc_date_time)
        self.assertIsNotNone(self.customer.forgot_password_key_value)
        self.assertIsNotNone(self.customer.fs_user_code_value)
        self.assertIsNotNone(self.customer.is_active)
        self.assertIsNotNone(self.customer.is_email_allowed)
        self.assertIsNotNone(self.customer.is_email_confirmed)
        self.assertIsNotNone(self.customer.is_email_marketing_allowed)
        self.assertIsNotNone(self.customer.is_locked)
        self.assertIsNotNone(self.customer.is_multiple_organizations_allowed)
        self.assertIsNotNone(self.customer.is_verbose_logging_forced)
        self.assertIsNotNone(self.customer.last_login_utc_date_time)
        self.assertIsNotNone(self.customer.last_name)
        self.assertIsNotNone(self.customer.password)
        self.assertIsNotNone(self.customer.phone)
        self.assertIsNotNone(self.customer.province)
        self.assertIsNotNone(self.customer.registration_utc_date_time)
        self.assertIsNotNone(self.customer.tac) #tac_id
        self.assertIsNotNone(self.customer.utc_offset_in_minutes)
        self.assertIsNotNone(self.customer.zip)
