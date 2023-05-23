from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .pac import Pac #pac_id
import api.models.constants.date_greater_than_filter as DateGreaterThanFilterConstants
class DateGreaterThanFilter(models.Model):  
    date_greater_than_filter_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True, unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
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
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(DateGreaterThanFilter, self).save(*args, **kwargs)
