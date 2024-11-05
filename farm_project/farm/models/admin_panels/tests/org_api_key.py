from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import OrgApiKey
from farm.models.admin_panels import OrgApiKeyAdmin
from farm.models.factories import OrgApiKeyFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class OrgApiKeyAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = OrgApiKeyAdmin(OrgApiKey, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('org_api_key_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'org_api_key_id',
            'api_key_value',
            'created_by',
            'created_utc_date_time',
            'expiration_utc_date_time',
            'is_active',
            'is_temp_user_key',
            'name',
            'organization_id',
            'org_customer_id',
            'code',
            )
        )
    def test_queryset(self):
        org_api_key = OrgApiKeyFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(org_api_key.code, [obj.code for obj in queryset])
