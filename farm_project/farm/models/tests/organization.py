# farm/models/tests/test_organization.py
from django.test import TestCase
from farm.models import Organization
from farm.models.factories import OrganizationFactory
from farm.models import CurrentRuntime
class OrganizationTestCase(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.organization = OrganizationFactory.create()
    def test_organization_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.organization)
    def test_organization_fields(self):
        self.assertIsInstance(self.organization, Organization)
        self.assertIsNotNone(self.organization.organization_id)
        self.assertIsNotNone(self.organization.code)
        self.assertIsNotNone(self.organization.insert_utc_date_time)
        self.assertIsNotNone(self.organization.last_update_utc_date_time)
        self.assertIsNotNone(self.organization.insert_user_id)
        self.assertIsNotNone(self.organization.last_update_user_id)
        self.assertIsNotNone(self.organization.last_change_code)
        self.assertIsNotNone(self.organization.name)
        self.assertIsNotNone(self.organization.tac) #tac_id
