from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from api.models import DateGreaterThanFilter
from api.models.admin_panels import DateGreaterThanFilterAdmin

class MockRequest:
    pass

class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True

request = MockRequest()
request.user = MockSuperUser()

class DateGreaterThanFilterAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = DateGreaterThanFilterAdmin(DateGreaterThanFilter, self.site)

    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('date_greater_than_filter_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )

    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ('date_greater_than_filter_id',
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
        date_greater_than_filter = DateGreaterThanFilter.objects.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(date_greater_than_filter, queryset)