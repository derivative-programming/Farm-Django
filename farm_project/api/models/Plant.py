from django.db import models
from django.utils import timezone
import datetime
import uuid 
from .flavor import Flavor #flavor_id
from .land import Land      #land_id
 
class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #flavor_id = models.IntegerField(null=True)
    flavor = models.ForeignKey(Flavor, related_name='plant_list', on_delete=models.SET_NULL, blank=True, null=True)
    is_delete_allowed = models.BooleanField(null=True)
    is_edit_allowed = models.BooleanField(null=True)	
    #land_id = models.IntegerField(null=True)
    land = models.ForeignKey(Land, related_name='plant_list', on_delete=models.SET_NULL, blank=True, null=True)	
    other_flavor = models.TextField(max_length=50)
    some_big_int_val = models.BigIntegerField(null=True)
    some_bit_val = models.BooleanField(null=True)
    some_date_val = models.DateField(null=True)
    some_decimal_val = models.DecimalField(max_digits=18, decimal_places=6,null=True)
    some_email_address = models.TextField(max_length=50)
    some_float_val = models.FloatField(null=True)	
    some_int_val = models.IntegerField(null=True)	
    some_money_val = models.DecimalField(max_digits=19, decimal_places=4,null=True)
    some_n_var_char_val = models.TextField(max_length=50)
    some_phone_number = models.TextField(max_length=50)
    some_text_val = models.TextField(max_length=max)
    some_uniqueidentifier_val = models.UUIDField(null=True)
    some_utc_date_time_val = models.DateTimeField(null=True)
    some_var_char_val = models.TextField(max_length=50)  

    def __str__(self):
        return str(self.code)