from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .flavor import Flavor #flavor_id
from .land import Land #land_id
import farm.models.constants.plant as PlantConstants
import logging 
from farm.models.managers import FlavorManager,FlavorEnum #flavor_id
from farm.models.managers import LandManager,LandEnum #land_id
from farm.models.managers import PlantManager,PlantEnum
from decimal import Decimal
from farm.helpers import TypeConversion


class Plant(models.Model):  
    plant_id = models.AutoField(primary_key=True,db_column='plant_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now,db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=timezone.now,db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    #flavor_id = models.IntegerField(null=True)
    flavor = models.ForeignKey(Flavor,
                               related_name='plant_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='flavor_id',
                               db_index=True)
    is_delete_allowed = models.BooleanField(
                                null=True,
                                db_column='is_delete_allowed',
                                db_index=PlantConstants.is_delete_allowed_calculatedIsDBColumnIndexed)
    is_edit_allowed = models.BooleanField(
                                null=True,
                                db_column='is_edit_allowed',
                                db_index=PlantConstants.is_edit_allowed_calculatedIsDBColumnIndexed)
    #land_id = models.IntegerField(null=True)
    land = models.ForeignKey(Land,
                               related_name='plant_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='land_id',
                               db_index=True)
    other_flavor = models.TextField(
                                null=True,
                                db_column='other_flavor',
                                db_index=PlantConstants.other_flavor_calculatedIsDBColumnIndexed)
    some_big_int_val = models.BigIntegerField(
                                null=True,
                                db_column='some_big_int_val',
                                db_index=PlantConstants.some_big_int_val_calculatedIsDBColumnIndexed)
    some_bit_val = models.BooleanField(
                                null=True,
                                db_column='some_bit_val',
                                db_index=PlantConstants.some_bit_val_calculatedIsDBColumnIndexed)
    some_date_val = models.DateField(
                                null=True,
                                db_column='some_date_val',
                                db_index=PlantConstants.some_date_val_calculatedIsDBColumnIndexed)
    some_decimal_val = models.DecimalField(
                                max_digits=18,
                                decimal_places=6,
                                db_column='some_decimal_val',
                                null=True,
                                db_index=PlantConstants.some_decimal_val_calculatedIsDBColumnIndexed)
    some_email_address = models.TextField(
                                max_length=50,
                                null=True,
                                db_column='some_email_address',
                                db_index=PlantConstants.some_email_address_calculatedIsDBColumnIndexed)
    some_float_val = models.FloatField(
                                null=True,
                                db_column='some_float_val',
                                db_index=PlantConstants.some_float_val_calculatedIsDBColumnIndexed)	
    some_int_val = models.IntegerField(
                                null=True,
                                db_column='some_int_val',
                                db_index=PlantConstants.some_int_val_calculatedIsDBColumnIndexed)	
    some_money_val = models.DecimalField(
                                max_digits=19,
                                decimal_places=4,
                                db_column='some_money_val',
                                null=True,
                                db_index=PlantConstants.some_money_val_calculatedIsDBColumnIndexed)
    some_n_var_char_val = models.TextField(
                                null=True,
                                db_column='some_n_var_char_val',
                                db_index=PlantConstants.some_n_var_char_val_calculatedIsDBColumnIndexed)
    some_phone_number = models.TextField(
                                max_length=50,
                                null=True,
                                db_column='some_phone_number',
                                db_index=PlantConstants.some_phone_number_calculatedIsDBColumnIndexed)
    some_text_val = models.TextField(
                                max_length=max,
                                null=True,
                                db_column='some_text_val',
                                db_index=False)
    some_uniqueidentifier_val = models.UUIDField(
                                null=True,
                                db_column='some_uniqueidentifier_val',
                                db_index=PlantConstants.some_uniqueidentifier_val_calculatedIsDBColumnIndexed)
    some_utc_date_time_val = models.DateTimeField(
                                null=True,
                                db_column='some_utc_date_time_val',
                                db_index=PlantConstants.some_utc_date_time_val_calculatedIsDBColumnIndexed)
    some_var_char_val = models.TextField(
                                max_length=50,
                                null=True,
                                db_column='some_var_char_val',
                                db_index=PlantConstants.some_var_char_val_calculatedIsDBColumnIndexed)
        
    objects = PlantManager()

    class Meta:
        db_table = 'farm_plant'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.plant_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:Plant = Plant.objects.get(plant_id=self.plant_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.plant_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Plant, self).save(*args, **kwargs)

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=false,calculatedIsParentObjectAvailable=true]Start   
    @staticmethod
    def build(land:Land
        ):
        item = Plant()
        item.code = uuid.uuid4()
        item.insert_utc_date_time = timezone.now
        item.last_update_utc_date_time = timezone.now
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.some_int_val = 0
        item.some_big_int_val = 0
        item.some_bit_val = False
        item.is_edit_allowed = False
        item.is_delete_allowed = False
        item.some_float_val = 0
        item.some_decimal_val = Decimal(0)
        item.some_utc_date_time_val = TypeConversion.get_default_date_time()
        item.some_date_val = TypeConversion.get_default_date()
        item.some_money_val = 0
        item.some_n_var_char_val = ""
        item.some_var_char_val = ""
        item.some_text_val = ""
        item.some_phone_number = ""
        item.some_email_address = ""
        item.some_uniqueidentifier_val = uuid.UUID(int=0)
        item.flavor = Flavor.objects.from_enum(enum_val=FlavorEnum.Unknown)
        item.land = land
        item.other_flavor = ""
        return item

    @staticmethod
    def initialize():
        pass
##GENLearn[isLookup=false,calculatedIsParentObjectAvailable=true]End
##GENTrainingBlock[caselookup]End