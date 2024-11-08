from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import DateGreaterThanFilter
from farm.models.admin_panels import DateGreaterThanFilterAdmin
from farm.models.factories import DateGreaterThanFilterFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class DateGreaterThanFilterAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
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
            ( 'date_greater_than_filter_id',
            'day_count',
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
        date_greater_than_filter = DateGreaterThanFilterFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(date_greater_than_filter.code, [obj.code for obj in queryset])
