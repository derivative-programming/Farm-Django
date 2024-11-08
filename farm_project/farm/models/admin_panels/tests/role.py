from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import Role
from farm.models.admin_panels import RoleAdmin
from farm.models.factories import RoleFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class RoleAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = RoleAdmin(Role, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('role_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'role_id',
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',
            'code',
            )
        )
    def test_queryset(self):
        role = RoleFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(role.code, [obj.code for obj in queryset])
