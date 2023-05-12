from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from api.models import TriStateFilter
from api.models.admin_panels import TriStateFilterAdmin

class MockRequest:
    pass

class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True

request = MockRequest()
request.user = MockSuperUser()

class TriStateFilterAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = TriStateFilterAdmin(TriStateFilter, self.site)

    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('tri_state_filter_id', 'code', 'insert_utc_date_time', 'last_udpate_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )

    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ('tri_state_filter_id',
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
        tri_state_filter = TriStateFilter.objects.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(tri_state_filter, queryset)