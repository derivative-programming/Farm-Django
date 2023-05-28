from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .pac import Pac #pac_id
import farm.models.constants.error_log as ErrorLogConstants
import logging
from farm.models.managers import PacManager,PacEnum #pac_id
from farm.models.managers import ErrorLogManager,ErrorLogEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class ErrorLog(models.Model):  
    error_log_id = models.AutoField(primary_key=True,db_column='error_log_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now,db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=timezone.now,db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    browser_code = models.UUIDField(
                                null=True,
                                db_column='browser_code',
                                db_index=ErrorLogConstants.browser_code_calculatedIsDBColumnIndexed)
    context_code = models.UUIDField(
                                null=True,
                                db_column='context_code',
                                db_index=ErrorLogConstants.context_code_calculatedIsDBColumnIndexed)
    created_utc_date_time = models.DateTimeField(
                                null=True,
                                db_column='created_utc_date_time',
                                db_index=ErrorLogConstants.created_utc_date_time_calculatedIsDBColumnIndexed)
    description = models.TextField(
                                null=True,
                                db_column='description',
                                db_index=ErrorLogConstants.description_calculatedIsDBColumnIndexed)
    is_client_side_error = models.BooleanField(
                                null=True,
                                db_column='is_client_side_error',
                                db_index=ErrorLogConstants.is_client_side_error_calculatedIsDBColumnIndexed)
    is_resolved = models.BooleanField(
                                null=True,
                                db_column='is_resolved',
                                db_index=ErrorLogConstants.is_resolved_calculatedIsDBColumnIndexed)
    #pac_id = models.IntegerField(null=True)
    pac = models.ForeignKey(Pac,
                               related_name='error_log_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='pac_id',
                               db_index=True)
    url = models.TextField(
                                null=True,
                                db_column='url',
                                db_index=ErrorLogConstants.url_calculatedIsDBColumnIndexed)
    objects = ErrorLogManager()
    class Meta:
        db_table = 'farm_error_log'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.error_log_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:ErrorLog = ErrorLog.objects.get(error_log_id=self.error_log_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.error_log_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(ErrorLog, self).save(*args, **kwargs)


   
    @staticmethod
    def build(pac:Pac
        ):
        item = ErrorLog()
        item.code = uuid.uuid4()
        item.insert_utc_date_time = timezone.now
        item.last_update_utc_date_time = timezone.now
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.browser_code = uuid.UUID(int=0)
        item.context_code = uuid.UUID(int=0)
        item.created_utc_date_time = TypeConversion.get_default_date_time()
        item.description = ""
        item.is_client_side_error = False
        item.is_resolved = False
        item.pac = pac #pac_id
        item.url = ""
        return item
    @staticmethod
    def initialize():
        pass

