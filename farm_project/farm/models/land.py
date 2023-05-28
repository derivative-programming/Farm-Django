from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .pac import Pac #pac_id
import farm.models.constants.land as LandConstants
import logging
from farm.models.managers import PacManager,PacEnum #pac_id
from farm.models.managers import LandManager,LandEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class Land(models.Model):  
    land_id = models.AutoField(primary_key=True,db_column='land_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now,db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=timezone.now,db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    description = models.TextField(
                                null=True,
                                db_column='description',
                                db_index=LandConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_column='display_order',
                                db_index=LandConstants.display_order_calculatedIsDBColumnIndexed)	
    is_active = models.BooleanField(
                                null=True,
                                db_column='is_active',
                                db_index=LandConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_column='lookup_enum_name',
                                db_index=LandConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_column='name',
                                db_index=LandConstants.name_calculatedIsDBColumnIndexed)
    #pac_id = models.IntegerField(null=True)
    pac = models.ForeignKey(Pac,
                               related_name='land_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='pac_id',
                               db_index=True)
    objects = LandManager()
    class Meta:
        db_table = 'farm_land'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.land_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:Land = Land.objects.get(land_id=self.land_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.land_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Land, self).save(*args, **kwargs)
  #vrdebug
    @staticmethod
    def build(pac:Pac
        ):
        item = Land()
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
        if Land.objects.filter(lookup_enum_name=LandEnum.Unknown.value).exists() == False:
            item = Land.build(pac)
            item.name = "Unknown"
            item.lookup_enum_name = "Unknown"
            item.description = "Unknown"
            item.display_order = Land.objects.count()
            item.is_active = True
            # item. = 1
            item.save()
        if Land.objects.filter(lookup_enum_name=LandEnum.Field_One.value).exists() == False:
            item = Land.build(pac)
            item.name = "Field One"
            item.lookup_enum_name = "Field_One"
            item.description = "Field One"
            item.display_order = Land.objects.count()
            item.is_active = True
            # item. = 1
            item.save()



