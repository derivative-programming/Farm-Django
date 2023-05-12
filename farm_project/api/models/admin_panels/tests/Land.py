from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from api.models import Land
from api.models.admin_panels import LandAdmin

class MockRequest:
    pass

class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True

request = MockRequest()
request.user = MockSuperUser()

class LandAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = LandAdmin(Land, self.site)

    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('land_id', 'code', 'insert_utc_date_time', 'last_udpate_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )

    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ('land_id',
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
        land = Land.objects.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(land, queryset)