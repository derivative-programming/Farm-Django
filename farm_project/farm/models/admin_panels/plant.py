# models/admin_panels/plant.py
"""
This module initializes the plant admin panel used in the project.
"""
from django.contrib import admin
class PlantAdmin(admin.ModelAdmin):
    """
    This class initializes the plant admin panel used in the project.
    """
    readonly_fields = (
        'plant_id',
        'code',
        'insert_utc_date_time',
        'last_update_utc_date_time',
        'insert_user_id',
        'last_update_user_id',
        'last_change_code')
    list_display = (
        'plant_id',
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
