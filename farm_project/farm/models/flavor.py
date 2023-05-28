from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .pac import Pac #pac_id
import farm.models.constants.flavor as FlavorConstants
import logging
from farm.models.managers import PacManager,PacEnum #pac_id
from farm.models.managers import FlavorManager,FlavorEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class Flavor(models.Model):  
    flavor_id = models.AutoField(primary_key=True,db_column='flavor_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now,db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=timezone.now,db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    description = models.TextField(
                                null=True,
                                db_column='description',
                                db_index=FlavorConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_column='display_order',
                                db_index=FlavorConstants.display_order_calculatedIsDBColumnIndexed)	
    is_active = models.BooleanField(
                                null=True,
                                db_column='is_active',
                                db_index=FlavorConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_column='lookup_enum_name',
                                db_index=FlavorConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_column='name',
                                db_index=FlavorConstants.name_calculatedIsDBColumnIndexed)
    #pac_id = models.IntegerField(null=True)
    pac = models.ForeignKey(Pac,
                               related_name='flavor_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='pac_id',
                               db_index=True)
    objects = FlavorManager()
    class Meta:
        db_table = 'farm_flavor'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.flavor_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:Flavor = Flavor.objects.get(flavor_id=self.flavor_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.flavor_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Flavor, self).save(*args, **kwargs)
    
    @staticmethod
    def build(pac:Pac
        ):
        item = Flavor()
        item.description = ""
        item.display_order = 0
        item.code = uuid.uuid4()
        item.insert_utc_date_time = timezone.now
        item.last_update_utc_date_time = timezone.now
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.is_active = False
        item.lookup_enum_name = ""
        item.name = ""
        #pac_id = models.IntegerField(null=True)
        item.pac = pac
        return item
    @staticmethod
    def initialize():
        pac = Pac.objects.all().first()
        if Flavor.objects.filter(lookup_enum_name=FlavorEnum.Unknown.value).exists() == False:
            item = Flavor.build(pac)
            item.name = "Unknown"
            item.lookup_enum_name = "Unknown"
            item.description = "Unknown"
            item.display_order = Flavor.objects.count()
            item.is_active = True
            # item. = 1
            item.save()
        if Flavor.objects.filter(lookup_enum_name=FlavorEnum.Sweet.value).exists() == False:
            item = Flavor.build(pac)
            item.name = "Sweet"
            item.lookup_enum_name = "Sweet"
            item.description = "Sweet"
            item.display_order = Flavor.objects.count()
            item.is_active = True
            # item. = 1
            item.save()
        if Flavor.objects.filter(lookup_enum_name=FlavorEnum.Sour.value).exists() == False:
            item = Flavor.build(pac)
            item.name = "Sour"
            item.lookup_enum_name = "Sour"
            item.description = "Sour"
            item.display_order = Flavor.objects.count()
            item.is_active = True
            # item. = 1
            item.save()


 


