from django.db import models
from django.utils import timezone
import datetime
import uuid
from .Organization import Organization
from .OrgCustomer import OrgCustomer

 
   
    
  
     


class OrgApiKey(models.Model):
    org_api_key_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    api_key_value = models.TextField(max_length=4000)
    created_by = models.TextField(max_length=100)
    created_utc_date_time = models.DateTimeField(null=True)
    expiration_utc_date_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(null=True)
    is_temp_user_key = models.BooleanField(null=True)
    name = models.TextField(max_length=100)	
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization, related_name='org_api_key_list', on_delete=models.SET_NULL, blank=True, null=True)	
    #org_customer_id = models.IntegerField(null=True)
    org_customer = models.ForeignKey(OrgCustomer, related_name='org_api_key_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)