from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import Tac
from farm.models.admin_panels import TacAdmin
from farm.models.factories import TacFactory
from farm.models import CurrentRuntime
class MockRequest:
    pass
class MockSuperUser:
    def has_perm(self, perm, obj=None):
        return True
request = MockRequest()
request.user = MockSuperUser()
class TacAdminTest(TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = TacAdmin(Tac, self.site)
    def test_readonly_fields(self):
        self.assertEqual(
            self.admin.readonly_fields,
            ('tac_id', 'code', 'insert_utc_date_time', 'last_update_utc_date_time', 'insert_user_id', 'last_update_user_id', 'last_change_code')
        )
    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display,
            ( 'tac_id',
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
        tac = TacFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(tac.code, [obj.code for obj in queryset])
