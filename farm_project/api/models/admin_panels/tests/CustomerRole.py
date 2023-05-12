from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from api.models import CustomerRole
from api.models.admin_panels import CustomerRoleAdmin

class MockRequest:
    pass

class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True

request = MockRequest()
request.user = MockSuperUser()

class CustomerRoleAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = CustomerRoleAdmin(CustomerRole, self.site)

    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('customer_role_id', 'code', 'insert_utc_date_time', 'last_udpate_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )

    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 
            'customer_role_id',
            'customer_id',
            'is_placeholder',
            'placeholder',
            'role_id',
            'code', 
            )
        )

    def test_queryset(self):
        customer_role = CustomerRole.objects.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(customer_role, queryset)