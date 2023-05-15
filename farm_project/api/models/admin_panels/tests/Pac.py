from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from api.models import Pac
from api.models.admin_panels import PacAdmin
from api.models.factories import PacFactory
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class PacAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = PacAdmin(Pac, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('pac_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'pac_id',
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'code', 
            )
        )
    def test_queryset(self):
        pac = PacFactory.create()
        queryset = self.admin.get_queryset(request) 
        self.assertIn(pac.code, [obj.code for obj in queryset]) 
