from django.db import models
from django.utils import timezone
import datetime
import uuid 
from .Customer import Customer
from .Organization import Organization

  
  

class OrgCustomer(models.Model):
    org_customer_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #customer_id = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer, related_name='org_customer_list', on_delete=models.SET_NULL, blank=True, null=True)	
    email = models.TextField(max_length=100)	
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization, related_name='org_customer_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)