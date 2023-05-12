from django.db import models
from django.utils import timezone
import datetime
import uuid
from .Pac import Pac

  
class DateGreaterThanFilter(models.Model):
    date_greater_than_filter_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    day_count = models.IntegerField(null=True)
    description = models.TextField(max_length=500)	
    display_order = models.IntegerField(null=True)	
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=100)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='date_greater_than_filter_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)
