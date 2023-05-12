from django.db import models
from django.utils import timezone
import datetime
import uuid 
from .Customer import Customer
from .Role import Role

  
class CustomerRole(models.Model):
    customer_role_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #customer_id = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer, related_name='customer_role_list', on_delete=models.SET_NULL, blank=True, null=True)	
    is_placeholder = models.BooleanField(null=True)
    placeholder = models.BooleanField(null=True)	
    #role_id = models.IntegerField(null=True)
    role = models.ForeignKey(Role, related_name='customer_role_list', on_delete=models.SET_NULL, blank=True, null=True)	  

    def __str__(self):
        return str(self.code)
