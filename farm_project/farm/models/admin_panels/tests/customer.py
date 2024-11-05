from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import Customer
from farm.models.admin_panels import CustomerAdmin
from farm.models.factories import CustomerFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class CustomerAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = CustomerAdmin(Customer, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('customer_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'customer_id',
            'active_organization_id',
            'email',
            'email_confirmed_utc_date_time',
            'first_name',
            'forgot_password_key_expiration_utc_date_time',
            'forgot_password_key_value',
            'fs_user_code_value',
            'is_active',
            'is_email_allowed',
            'is_email_confirmed',
            'is_email_marketing_allowed',
            'is_locked',
            'is_multiple_organizations_allowed',
            'is_verbose_logging_forced',
            'last_login_utc_date_time',
            'last_name',
            'password',
            'phone',
            'province',
            'registration_utc_date_time',
            'tac_id',
            'utc_offset_in_minutes',
            'zip',
            'code',
            )
        )
    def test_queryset(self):
        customer = CustomerFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(customer.code, [obj.code for obj in queryset])
