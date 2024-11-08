from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import OrgCustomer
from farm.models.admin_panels import OrgCustomerAdmin
from farm.models.factories import OrgCustomerFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class OrgCustomerAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = OrgCustomerAdmin(OrgCustomer, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('org_customer_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'org_customer_id',
            'customer_id',
            'email',
            'organization_id',
            'code',
            )
        )
    def test_queryset(self):
        org_customer = OrgCustomerFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(org_customer.code, [obj.code for obj in queryset])
