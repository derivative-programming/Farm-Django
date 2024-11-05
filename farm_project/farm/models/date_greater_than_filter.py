from django.db import models
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
import uuid
from .pac import Pac #pac_id
import farm.models.constants.date_greater_than_filter as DateGreaterThanFilterConstants
from farm.models.managers import DateGreaterThanFilterManager,DateGreaterThanFilterEnum 

class DateGreaterThanFilter(models.Model):  
    date_greater_than_filter_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True, unique=True)
    insert_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc))
    last_update_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc))
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    day_count = models.IntegerField(
                                null=True,
                                db_index=DateGreaterThanFilterConstants.day_count_calculatedIsDBColumnIndexed)	
    description = models.TextField(
                                null=True,
                                db_index=DateGreaterThanFilterConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_index=DateGreaterThanFilterConstants.display_order_calculatedIsDBColumnIndexed)	
    is_active = models.BooleanField(
                                null=True,
                                db_index=DateGreaterThanFilterConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_index=DateGreaterThanFilterConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_index=DateGreaterThanFilterConstants.name_calculatedIsDBColumnIndexed)
    #pac_id = models.IntegerField(null=True)
    pac = models.ForeignKey(Pac,
                               related_name='date_greater_than_filter_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_index=True)
        
    objects = DateGreaterThanFilterManager()
    
    class Meta:
        db_table = 'farm_date_greater_than_filter'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.date_greater_than_filter_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance = DateGreaterThanFilter.objects.get(date_greater_than_filter_id=self.date_greater_than_filter_id)
            if self.last_change_code != current_instance.last_change_code:
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.date_greater_than_filter_id is None:
            self.insert_utc_date_time = datetime.now(timezone.utc)
        self.last_update_utc_date_time = datetime.now(timezone.utc)
        self.last_change_code = uuid.uuid4()
        return super(DateGreaterThanFilter, self).save(*args, **kwargs)



##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=true]Start    
    def get_parent_object(self):
        return self.pac
    @staticmethod
    def build(pac:Pac
        ):
        item = DateGreaterThanFilter()
        item.day_count = 0
        item.code = uuid.uuid4()
        item.insert_utc_date_time = datetime.now(timezone.utc)
        item.last_update_utc_date_time = datetime.now(timezone.utc)
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.description = ""
        item.display_order = 0
        item.is_active = False
        item.lookup_enum_name = ""
        item.name = ""
        #pac_id = models.IntegerField(null=True)
        item.pac = pac
        return item


    @staticmethod
    def initialize():
        pac = Pac.objects.all().first()
        if DateGreaterThanFilter.objects.filter(lookup_enum_name=DateGreaterThanFilterEnum.Unknown.value).exists() == False:
            item = DateGreaterThanFilter.build(pac) 
            item.name = "Unknown"
            item.lookup_enum_name = "Unknown"
            item.description = "Unknown"
            item.display_order = DateGreaterThanFilter.objects.count()
            item.is_active = True
            # item.day_count = 1
            item.save()
        if DateGreaterThanFilter.objects.filter(lookup_enum_name=DateGreaterThanFilterEnum.Last_24_Hours.value).exists() == False:
            item = DateGreaterThanFilter.build(pac)  
            item.name = "Last 24 Hours"
            item.lookup_enum_name = "Last_24_Hours"
            item.description = "Last 24 Hours"
            item.display_order = DateGreaterThanFilter.objects.count()
            item.is_active = True
            # item.day_count = 1
            item.save()
        if DateGreaterThanFilter.objects.filter(lookup_enum_name=DateGreaterThanFilterEnum.Last_7_Days.value).exists() == False:
            item = DateGreaterThanFilter.build(pac) 
            item.name = "Last 7 Days"
            item.lookup_enum_name = "Last_7_Days"
            item.description = "Last 7 Days"
            item.display_order = DateGreaterThanFilter.objects.count()
            item.is_active = True
            # item.day_count = 7
            item.save()
        if DateGreaterThanFilter.objects.filter(lookup_enum_name=DateGreaterThanFilterEnum.Last_30_Days.value).exists() == False:
            item = DateGreaterThanFilter.build(pac) 
            item.name = "Last 30 Days"
            item.lookup_enum_name = "Last_30_Days"
            item.description = "Last 30 Days"
            item.display_order = DateGreaterThanFilter.objects.count()
            item.is_active = True
            # item.day_count = 30
            item.save()
        if DateGreaterThanFilter.objects.filter(lookup_enum_name=DateGreaterThanFilterEnum.Last_90_Days.value).exists() == False:
            item = DateGreaterThanFilter.build(pac)  
            item.name = "Last 90 Days"
            item.lookup_enum_name = "Last_90_Days"
            item.description = "Last 90 Days"
            item.display_order = DateGreaterThanFilter.objects.count()
            item.is_active = True
            # item.day_count = 90
            item.save()
        if DateGreaterThanFilter.objects.filter(lookup_enum_name=DateGreaterThanFilterEnum.Last_365_Days.value).exists() == False:
            item = DateGreaterThanFilter.build(pac) 
            item.name = "Last 365 Days"
            item.lookup_enum_name = "Last_365_Days"
            item.description = "Last 365 Days"
            item.display_order = DateGreaterThanFilter.objects.count()
            item.is_active = True
            # item.day_count = 365
            item.save() 
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=true]End
##GENTrainingBlock[caselookup]End