from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .pac import Pac #pac_id
import farm.models.constants.tri_state_filter as TriStateFilterConstants
import logging
from farm.models.managers import PacManager,PacEnum #pac_id
from farm.models.managers import TriStateFilterManager,TriStateFilterEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class TriStateFilter(models.Model):  
    tri_state_filter_id = models.AutoField(primary_key=True,db_column='tri_state_filter_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now,db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=timezone.now,db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    description = models.TextField(
                                null=True,
                                db_column='description',
                                db_index=TriStateFilterConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_column='display_order',
                                db_index=TriStateFilterConstants.display_order_calculatedIsDBColumnIndexed)	
    is_active = models.BooleanField(
                                null=True,
                                db_column='is_active',
                                db_index=TriStateFilterConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_column='lookup_enum_name',
                                db_index=TriStateFilterConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_column='name',
                                db_index=TriStateFilterConstants.name_calculatedIsDBColumnIndexed)
    #pac_id = models.IntegerField(null=True)
    pac = models.ForeignKey(Pac,
                               related_name='tri_state_filter_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='pac_id',
                               db_index=True)
    state_int_value = models.IntegerField(
                                null=True,
                                db_column='state_int_value',
                                db_index=TriStateFilterConstants.state_int_value_calculatedIsDBColumnIndexed)	
    objects = TriStateFilterManager()
    class Meta:
        db_table = 'farm_tri_state_filter'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.tri_state_filter_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:TriStateFilter = TriStateFilter.objects.get(tri_state_filter_id=self.tri_state_filter_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.tri_state_filter_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(TriStateFilter, self).save(*args, **kwargs)
    
    @staticmethod
    def build(pac:Pac
        ):
        item = TriStateFilter()
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
        item.state_int_value = 0
        item.code = uuid.uuid4()
        item.insert_utc_date_time = timezone.now
        item.last_update_utc_date_time = timezone.now
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.pac = pac
        return item
    @staticmethod
    def initialize():
        pac = Pac.objects.all().first()
        if TriStateFilter.objects.filter(lookup_enum_name=TriStateFilterEnum.Unknown.value).exists() == False:
            item = TriStateFilter.build(pac)
            item.name = ""
            item.lookup_enum_name = "Unknown"
            item.description = ""
            item.display_order = TriStateFilter.objects.count()
            item.is_active = True
            # item.state_int_value = 1
            item.save()
        if TriStateFilter.objects.filter(lookup_enum_name=TriStateFilterEnum.Yes.value).exists() == False:
            item = TriStateFilter.build(pac)
            item.name = "Yes"
            item.lookup_enum_name = "Yes"
            item.description = "Yes"
            item.display_order = TriStateFilter.objects.count()
            item.is_active = True
            # item.state_int_value = 1
            item.save()
        if TriStateFilter.objects.filter(lookup_enum_name=TriStateFilterEnum.No.value).exists() == False:
            item = TriStateFilter.build(pac)
            item.name = "No"
            item.lookup_enum_name = "No"
            item.description = "No"
            item.display_order = TriStateFilter.objects.count()
            item.is_active = True
            # item.state_int_value = 1
            item.save()



