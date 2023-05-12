from django.db import models
from django.utils import timezone
import datetime
import uuid 
from .Tac import Tac

  
class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    name = models.TextField(max_length=100)	
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac, related_name='organization_list', on_delete=models.SET_NULL, blank=True, null=True)
	  

    def __str__(self):
        return str(self.code)
    