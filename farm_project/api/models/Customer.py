from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .tac import Tac #tac_id
from api.models.constants import CustomerConstants
class Customer(models.Model): 
    customerConstants = CustomerConstants()
    customer_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    active_organization_id = models.IntegerField(
                                null=True,
                                db_index=customerConstants.active_organization_id_calculatedIsDBColumnIndexed)	
    email = models.TextField(
                                max_length=50,
                                null=True,
                                db_index=customerConstants.email_calculatedIsDBColumnIndexed)
    email_confirmed_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=customerConstants.email_confirmed_utc_date_time_calculatedIsDBColumnIndexed)
    first_name = models.TextField(
                                null=True,
                                db_index=customerConstants.first_name_calculatedIsDBColumnIndexed)
    forgot_password_key_expiration_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=customerConstants.forgot_password_key_expiration_utc_date_time_calculatedIsDBColumnIndexed)
    forgot_password_key_value = models.TextField(
                                null=True,
                                db_index=customerConstants.forgot_password_key_value_calculatedIsDBColumnIndexed)
    fs_user_code_value = models.UUIDField(
                                null=True,
                                db_index=customerConstants.fs_user_code_value_calculatedIsDBColumnIndexed)
    is_active = models.BooleanField(
                                null=True,
                                db_index=customerConstants.is_active_calculatedIsDBColumnIndexed)
    is_email_allowed = models.BooleanField(
                                null=True,
                                db_index=customerConstants.is_email_allowed_calculatedIsDBColumnIndexed)
    is_email_confirmed = models.BooleanField(
                                null=True,
                                db_index=customerConstants.is_email_confirmed_calculatedIsDBColumnIndexed)
    is_email_marketing_allowed = models.BooleanField(
                                null=True,
                                db_index=customerConstants.is_email_marketing_allowed_calculatedIsDBColumnIndexed)
    is_locked = models.BooleanField(
                                null=True,
                                db_index=customerConstants.is_locked_calculatedIsDBColumnIndexed)
    is_multiple_organizations_allowed = models.BooleanField(
                                null=True,
                                db_index=customerConstants.is_multiple_organizations_allowed_calculatedIsDBColumnIndexed)
    is_verbose_logging_forced = models.BooleanField(
                                null=True,
                                db_index=customerConstants.is_verbose_logging_forced_calculatedIsDBColumnIndexed)
    last_login_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=customerConstants.last_login_utc_date_time_calculatedIsDBColumnIndexed)
    last_name = models.TextField(
                                null=True,
                                db_index=customerConstants.last_name_calculatedIsDBColumnIndexed)
    password = models.TextField(
                                null=True,
                                db_index=customerConstants.password_calculatedIsDBColumnIndexed)
    phone = models.TextField(
                                max_length=50,
                                null=True,
                                db_index=customerConstants.phone_calculatedIsDBColumnIndexed)
    province = models.TextField(
                                null=True,
                                db_index=customerConstants.province_calculatedIsDBColumnIndexed)
    registration_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=customerConstants.registration_utc_date_time_calculatedIsDBColumnIndexed)
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac,
                               related_name='customer_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_index=True)
    utc_offset_in_minutes = models.IntegerField(
                                null=True,
                                db_index=customerConstants.utc_offset_in_minutes_calculatedIsDBColumnIndexed)	
    zip = models.TextField(
                                null=True,
                                db_index=customerConstants.zip_calculatedIsDBColumnIndexed)
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.customer_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance = Customer.objects.get(customer_id=self.customer_id)
            if self.last_change_code != current_instance.last_change_code:
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.customer_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Customer, self).save(*args, **kwargs)
