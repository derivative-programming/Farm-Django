from django.db import models
from django.utils import timezone
import datetime
import uuid 
from .flavor import Flavor #flavor_id
from .land import Land      #land_id
from api.models.constants import PlantConstants
 
class Plant(models.Model): 
    plantConstants = PlantConstants()
    plant_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #flavor_id = models.IntegerField(null=True)
    flavor = models.ForeignKey(Flavor, 
                               related_name='plant_list', 
                               on_delete=models.SET_NULL, 
                               blank=True, 
                               null=True,
                               db_index=True)
    is_delete_allowed = models.BooleanField(
                                null=True,
                                db_index=plantConstants.is_delete_allowed_calculatedIsDBColumnIndexed)
    is_edit_allowed = models.BooleanField(
                                null=True,
                                db_index=plantConstants.is_edit_allowed_calculatedIsDBColumnIndexed)	
    #land_id = models.IntegerField(null=True)
    land = models.ForeignKey(Land, 
                                related_name='plant_list', 
                                on_delete=models.SET_NULL, 
                                blank=True, 
                                null=True,
                                db_index=True)	
    other_flavor = models.TextField(
                                null=True,
                                db_index=plantConstants.other_flavor_calculatedIsDBColumnIndexed)
    some_big_int_val = models.BigIntegerField(
                                null=True,
                                db_index=plantConstants.some_big_int_val_calculatedIsDBColumnIndexed)
    some_bit_val = models.BooleanField(
                                null=True,
                                db_index=plantConstants.some_bit_val_calculatedIsDBColumnIndexed)
    some_date_val = models.DateField(
                                null=True,
                                db_index=plantConstants.some_date_val_calculatedIsDBColumnIndexed)
    some_decimal_val = models.DecimalField(
                                max_digits=18, 
                                decimal_places=6,
                                null=True,
                                db_index=plantConstants.some_decimal_val_calculatedIsDBColumnIndexed)
    some_email_address = models.TextField(
                                max_length=50,
                                null=True,
                                db_index=plantConstants.some_email_address_calculatedIsDBColumnIndexed)
    some_float_val = models.FloatField(
                                null=True,
                                db_index=plantConstants.some_float_val_calculatedIsDBColumnIndexed)	
    some_int_val = models.IntegerField(
                                null=True,
                                db_index=plantConstants.some_int_val_calculatedIsDBColumnIndexed)	
    some_money_val = models.DecimalField(
                                max_digits=19, 
                                decimal_places=4,
                                null=True,
                                db_index=plantConstants.some_money_val_calculatedIsDBColumnIndexed)
    some_n_var_char_val = models.TextField(
                                max_length=50,
                                null=True,
                                db_index=plantConstants.some_n_var_char_val_calculatedIsDBColumnIndexed)
    some_phone_number = models.TextField(
                                max_length=50,
                                null=True,
                                db_index=plantConstants.some_phone_number_calculatedIsDBColumnIndexed)
    some_text_val = models.TextField(
                                max_length=max,
                                null=True,
                                db_index=False)
    some_uniqueidentifier_val = models.UUIDField(
                                null=True,
                                db_index=plantConstants.some_uniqueidentifier_val_calculatedIsDBColumnIndexed)
    some_utc_date_time_val = models.DateTimeField(
                                null=True,
                                db_index=plantConstants.some_utc_date_time_val_calculatedIsDBColumnIndexed)
    some_var_char_val = models.TextField(
                                max_length=50,
                                null=True,
                                db_index=plantConstants.some_var_char_val_calculatedIsDBColumnIndexed)  

    def __str__(self):
        return str(self.code)