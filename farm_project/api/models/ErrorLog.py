from django.db import models
from django.utils import timezone
import datetime
import uuid
from .Pac import Pac

  
class ErrorLog(models.Model):
    error_log_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    browser_code = models.UUIDField(null=True)
    context_code = models.UUIDField(null=True)
    created_utc_date_time = models.DateTimeField(null=True)
    description = models.TextField(max_length=max)
    is_client_side_error = models.BooleanField(null=True)
    is_resolved = models.BooleanField(null=True)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='error_log_list', on_delete=models.SET_NULL, blank=True, null=True)	
    url = models.TextField(max_length=500)   

    def __str__(self):
        return str(self.code)