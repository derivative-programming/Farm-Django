from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import Organization
from farm.models.admin_panels import OrganizationAdmin
from farm.models.factories import OrganizationFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class OrganizationAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = OrganizationAdmin(Organization, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('organization_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'organization_id',
            'name',
            'tac_id',
            'code', 
            )
        )
    def test_queryset(self):
        organization = OrganizationFactory.create()
        queryset = self.admin.get_queryset(request) 
        self.assertIn(organization.code, [obj.code for obj in queryset]) 
