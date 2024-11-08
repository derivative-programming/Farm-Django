# farm/models/tests/test_plant.py
"""
Tests for the Plant model.
"""
import logging
from django.test import TestCase
from farm.models import Plant
from farm.models.factories import PlantFactory
from farm.models import CurrentRuntime
class PlantTestCase(TestCase):
    """
    Test case for the Plant model.
    """
    def setUp(self):
        CurrentRuntime.initialize()
        self.plant = PlantFactory.create()
    def test_plant_creation(self):
        """
        Test that a plant instance was created.
        """
        # Test that the instance was created
        self.assertIsNotNone(self.plant)
    def test_plant_fields(self):
        """
        Test that the plant instance has all the fields.
        """
        self.assertIsInstance(self.plant, Plant)
        self.assertIsNotNone(self.plant.plant_id)
        self.assertIsNotNone(self.plant.code)
        self.assertIsNotNone(self.plant.insert_utc_date_time)
        self.assertIsNotNone(self.plant.last_update_utc_date_time)
        self.assertIsNotNone(self.plant.insert_user_id)
        self.assertIsNotNone(self.plant.last_update_user_id)
        self.assertIsNotNone(self.plant.last_change_code)
        self.assertIsNotNone(self.plant.flvr_foreign_key) #flvr_foreign_key_id
        self.assertIsNotNone(self.plant.is_delete_allowed)
        self.assertIsNotNone(self.plant.is_edit_allowed)
        self.assertIsNotNone(self.plant.land) #land_id
        self.assertIsNotNone(self.plant.other_flavor)
        self.assertIsNotNone(self.plant.some_big_int_val)
        self.assertIsNotNone(self.plant.some_bit_val)
        self.assertIsNotNone(self.plant.some_date_val)
        self.assertIsNotNone(self.plant.some_decimal_val)
        self.assertIsNotNone(self.plant.some_email_address)
        self.assertIsNotNone(self.plant.some_float_val)
        self.assertIsNotNone(self.plant.some_int_val)
        self.assertIsNotNone(self.plant.some_money_val)
        self.assertIsNotNone(self.plant.some_n_var_char_val)
        self.assertIsNotNone(self.plant.some_phone_number)
        self.assertIsNotNone(self.plant.some_text_val)
        self.assertIsNotNone(self.plant.some_uniqueidentifier_val)
        self.assertIsNotNone(self.plant.some_utc_date_time_val)
        self.assertIsNotNone(self.plant.some_var_char_val)
