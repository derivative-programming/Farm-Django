from django.db import models
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
import uuid
from .tac import Tac #tac_id
import farm.models.constants.customer as CustomerConstants
import logging
from farm.models.managers import TacManager,TacEnum #tac_id
from farm.models.managers import CustomerManager,CustomerEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True,db_column='customer_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')
    active_organization_id = models.IntegerField(
                                null=True,
                                db_column='active_organization_id',
                                db_index=CustomerConstants.active_organization_id_calculatedIsDBColumnIndexed)
    email = models.TextField(
                                max_length=50,
                                null=True,
                                db_column='email',
                                db_index=CustomerConstants.email_calculatedIsDBColumnIndexed)
    email_confirmed_utc_date_time = models.DateTimeField(
                                null=True,
                                db_column='email_confirmed_utc_date_time',
                                db_index=CustomerConstants.email_confirmed_utc_date_time_calculatedIsDBColumnIndexed)
    first_name = models.TextField(
                                null=True,
                                db_column='first_name',
                                db_index=CustomerConstants.first_name_calculatedIsDBColumnIndexed)
    forgot_password_key_expiration_utc_date_time = models.DateTimeField(
                                null=True,
                                db_column='forgot_password_key_expiration_utc_date_time',
                                db_index=CustomerConstants.forgot_password_key_expiration_utc_date_time_calculatedIsDBColumnIndexed)
    forgot_password_key_value = models.TextField(
                                null=True,
                                db_column='forgot_password_key_value',
                                db_index=CustomerConstants.forgot_password_key_value_calculatedIsDBColumnIndexed)
    fs_user_code_value = models.UUIDField(
                                null=True,
                                db_column='fs_user_code_value',
                                db_index=CustomerConstants.fs_user_code_value_calculatedIsDBColumnIndexed)
    is_active = models.BooleanField(
                                null=True,
                                db_column='is_active',
                                db_index=CustomerConstants.is_active_calculatedIsDBColumnIndexed)
    is_email_allowed = models.BooleanField(
                                null=True,
                                db_column='is_email_allowed',
                                db_index=CustomerConstants.is_email_allowed_calculatedIsDBColumnIndexed)
    is_email_confirmed = models.BooleanField(
                                null=True,
                                db_column='is_email_confirmed',
                                db_index=CustomerConstants.is_email_confirmed_calculatedIsDBColumnIndexed)
    is_email_marketing_allowed = models.BooleanField(
                                null=True,
                                db_column='is_email_marketing_allowed',
                                db_index=CustomerConstants.is_email_marketing_allowed_calculatedIsDBColumnIndexed)
    is_locked = models.BooleanField(
                                null=True,
                                db_column='is_locked',
                                db_index=CustomerConstants.is_locked_calculatedIsDBColumnIndexed)
    is_multiple_organizations_allowed = models.BooleanField(
                                null=True,
                                db_column='is_multiple_organizations_allowed',
                                db_index=CustomerConstants.is_multiple_organizations_allowed_calculatedIsDBColumnIndexed)
    is_verbose_logging_forced = models.BooleanField(
                                null=True,
                                db_column='is_verbose_logging_forced',
                                db_index=CustomerConstants.is_verbose_logging_forced_calculatedIsDBColumnIndexed)
    last_login_utc_date_time = models.DateTimeField(
                                null=True,
                                db_column='last_login_utc_date_time',
                                db_index=CustomerConstants.last_login_utc_date_time_calculatedIsDBColumnIndexed)
    last_name = models.TextField(
                                null=True,
                                db_column='last_name',
                                db_index=CustomerConstants.last_name_calculatedIsDBColumnIndexed)
    password = models.TextField(
                                null=True,
                                db_column='password',
                                db_index=CustomerConstants.password_calculatedIsDBColumnIndexed)
    phone = models.TextField(
                                max_length=50,
                                null=True,
                                db_column='phone',
                                db_index=CustomerConstants.phone_calculatedIsDBColumnIndexed)
    province = models.TextField(
                                null=True,
                                db_column='province',
                                db_index=CustomerConstants.province_calculatedIsDBColumnIndexed)
    registration_utc_date_time = models.DateTimeField(
                                null=True,
                                db_column='registration_utc_date_time',
                                db_index=CustomerConstants.registration_utc_date_time_calculatedIsDBColumnIndexed)
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac,
                               related_name='customer_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='tac_id',
                               db_index=True)
    utc_offset_in_minutes = models.IntegerField(
                                null=True,
                                db_column='utc_offset_in_minutes',
                                db_index=CustomerConstants.utc_offset_in_minutes_calculatedIsDBColumnIndexed)
    zip = models.TextField(
                                null=True,
                                db_column='zip',
                                db_index=CustomerConstants.zip_calculatedIsDBColumnIndexed)
    objects = CustomerManager()
    class Meta:
        db_table = 'farm_customer'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.customer_id is not None:
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:Customer = Customer.objects.get(customer_id=self.customer_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.customer_id is None:
            self.insert_utc_date_time = datetime.now(timezone.utc)
        self.last_update_utc_date_time = datetime.now(timezone.utc)
        self.last_change_code = uuid.uuid4()
        return super(Customer, self).save(*args, **kwargs)



    @staticmethod
    def build(tac:Tac
        ):
        item = Customer()
        item.code = uuid.uuid4()
        item.insert_utc_date_time = datetime.now(timezone.utc)
        item.last_update_utc_date_time = datetime.now(timezone.utc)
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.active_organization_id = 0
        item.email = ""
        item.email_confirmed_utc_date_time = TypeConversion.get_default_date_time()
        item.first_name = ""
        item.forgot_password_key_expiration_utc_date_time = TypeConversion.get_default_date_time()
        item.forgot_password_key_value = ""
        item.fs_user_code_value = uuid.UUID(int=0)
        item.is_active = False
        item.is_email_allowed = False
        item.is_email_confirmed = False
        item.is_email_marketing_allowed = False
        item.is_locked = False
        item.is_multiple_organizations_allowed = False
        item.is_verbose_logging_forced = False
        item.last_login_utc_date_time = TypeConversion.get_default_date_time()
        item.last_name = ""
        item.password = ""
        item.phone = ""
        item.province = ""
        item.registration_utc_date_time = TypeConversion.get_default_date_time()
        item.tac = tac #tac_id
        item.utc_offset_in_minutes = 0
        item.zip = ""
        return item
    @staticmethod
    def initialize():
        pass

