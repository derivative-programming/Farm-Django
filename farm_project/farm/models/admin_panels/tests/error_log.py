from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import ErrorLog
from farm.models.admin_panels import ErrorLogAdmin
from farm.models.factories import ErrorLogFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class ErrorLogAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = ErrorLogAdmin(ErrorLog, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('error_log_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'error_log_id',
            'browser_code',
            'context_code',
            'created_utc_date_time',
            'description',
            'is_client_side_error',
            'is_resolved',
            'pac_id',
            'url',
            'code',
            )
        )
    def test_queryset(self):
        error_log = ErrorLogFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(error_log.code, [obj.code for obj in queryset])
