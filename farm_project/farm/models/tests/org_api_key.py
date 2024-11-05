# farm/models/tests/test_org_api_key.py
from django.test import TestCase
from farm.models import OrgApiKey
from farm.models.factories import OrgApiKeyFactory
from farm.models import CurrentRuntime
class OrgApiKeyTestCase(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.org_api_key = OrgApiKeyFactory.create()
    def test_org_api_key_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.org_api_key)
    def test_org_api_key_fields(self):
        self.assertIsInstance(self.org_api_key, OrgApiKey)
        self.assertIsNotNone(self.org_api_key.org_api_key_id)
        self.assertIsNotNone(self.org_api_key.code)
        self.assertIsNotNone(self.org_api_key.insert_utc_date_time)
        self.assertIsNotNone(self.org_api_key.last_update_utc_date_time)
        self.assertIsNotNone(self.org_api_key.insert_user_id)
        self.assertIsNotNone(self.org_api_key.last_update_user_id)
        self.assertIsNotNone(self.org_api_key.last_change_code)
        self.assertIsNotNone(self.org_api_key.api_key_value)
        self.assertIsNotNone(self.org_api_key.created_by)
        self.assertIsNotNone(self.org_api_key.created_utc_date_time)
        self.assertIsNotNone(self.org_api_key.expiration_utc_date_time)
        self.assertIsNotNone(self.org_api_key.is_active)
        self.assertIsNotNone(self.org_api_key.is_temp_user_key)
        self.assertIsNotNone(self.org_api_key.name)
        self.assertIsNotNone(self.org_api_key.organization) #organization_id
        self.assertIsNotNone(self.org_api_key.org_customer) #org_customer_id
