from django.db import models
from django.utils import timezone
import datetime
import uuid
from .Tac import Tac

 
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time = models.DateTimeField(default=timezone.now)
    last_update_utc_date_time = models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)		
    active_organization_id = models.IntegerField(null=True)	
    email = models.TextField(max_length=100)
    email_confirmed_utc_date_time = models.DateTimeField(null=True)
    first_name = models.TextField(max_length=200)
    forgot_password_key_expiration_utc_date_time = models.DateTimeField(null=True)
    forgot_password_key_value = models.TextField(max_length=1000)
    fs_user_code_value = models.UUIDField(null=True)
    is_active = models.BooleanField(null=True)
    is_email_allowed = models.BooleanField(null=True)
    is_email_confirmed = models.BooleanField(null=True)
    is_email_marketing_allowed = models.BooleanField(null=True)
    is_locked = models.BooleanField(null=True)
    is_multiple_organizations_allowed = models.BooleanField(null=True)
    is_verbose_logging_forced = models.BooleanField(null=True)
    last_login_utc_date_time = models.DateTimeField(null=True)
    last_name = models.TextField(max_length=200)
    password = models.TextField(max_length=100)
    phone = models.TextField(max_length=50)
    province = models.TextField(max_length=50)
    registration_utc_date_time = models.DateTimeField(null=True)	
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac, related_name='customer_list', on_delete=models.SET_NULL, blank=True, null=True)	
    utc_offset_in_minutes = models.IntegerField(null=True)	
    zip = models.TextField(max_length=200)  

    def __str__(self):
        return str(self.code) 