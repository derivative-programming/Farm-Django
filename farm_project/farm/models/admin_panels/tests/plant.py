# models/admin_panels/tests/plant.py
"""
This module initializes the plant admin panel test used in the project.
"""
import logging
from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from farm.models import Plant
from farm.models.admin_panels import PlantAdmin
from farm.models.factories import PlantFactory
from farm.models import CurrentRuntime
class MockRequest:
    """
    This class initializes the mock request used in the project.
    """
class MockSuperUser:
    """
    This class initializes the mock super user used in the project.
    """
    def has_perm(self, perm, obj=None):
        """
        This method checks if the super user has permission.
        """
        return True
request = MockRequest()
request.user = MockSuperUser()
class PlantAdminTest(TestCase):
    """
    This class initializes the plant admin panel test used in the project.
    """
    def setUp(self):
        CurrentRuntime.initialize()
        self.site = AdminSite()
        self.admin = PlantAdmin(Plant, self.site)
    def test_readonly_fields(self):
        """
        This method tests the readonly fields of the plant admin panel.
        """
        self.assertEqual(
            self.admin.readonly_fields,
            ('plant_id',
             'code',
             'insert_utc_date_time',
             'last_update_utc_date_time',
             'insert_user_id',
             'last_update_user_id',
             'last_change_code')
        )
    def test_list_display(self):
        """
        This method tests the list display of the plant admin panel.
        """
        self.assertEqual(
            self.admin.list_display,
            ( 'plant_id',
            'flvr_foreign_key', #flvr_foreign_key_id
            'is_delete_allowed',
            'is_edit_allowed',
            'land_id',
            'other_flavor',
            'some_big_int_val',
            'some_bit_val',
            'some_date_val',
            'some_decimal_val',
            'some_email_address',
            'some_float_val',
            'some_int_val',
            'some_money_val',
            'some_n_var_char_val',
            'some_phone_number',
            'some_text_val',
            'some_uniqueidentifier_val',
            'some_utc_date_time_val',
            'some_var_char_val',
            'code',
            )
        )
    def test_queryset(self):
        """
        This method tests the queryset of the plant admin panel.
        """
        plant = PlantFactory.create()
        queryset = self.admin.get_queryset(request)
        self.assertIn(plant.code, [obj.code for obj in queryset])
