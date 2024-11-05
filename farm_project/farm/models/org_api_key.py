from django.db import models
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
import uuid
from .organization import Organization #organization_id
from .org_customer import OrgCustomer #org_customer_id
import farm.models.constants.org_api_key as OrgApiKeyConstants
import logging
from farm.models.managers import OrganizationManager,OrganizationEnum #organization_id
from farm.models.managers import OrgCustomerManager,OrgCustomerEnum #org_customer_id
from farm.models.managers import OrgApiKeyManager,OrgApiKeyEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class OrgApiKey(models.Model):
    org_api_key_id = models.AutoField(primary_key=True,db_column='org_api_key_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')
    api_key_value = models.TextField(
                                null=True,
                                db_column='api_key_value',
                                db_index=OrgApiKeyConstants.api_key_value_calculatedIsDBColumnIndexed)
    created_by = models.TextField(
                                null=True,
                                db_column='created_by',
                                db_index=OrgApiKeyConstants.created_by_calculatedIsDBColumnIndexed)
    created_utc_date_time = models.DateTimeField(
                                null=True,
                                db_column='created_utc_date_time',
                                db_index=OrgApiKeyConstants.created_utc_date_time_calculatedIsDBColumnIndexed)
    expiration_utc_date_time = models.DateTimeField(
                                null=True,
                                db_column='expiration_utc_date_time',
                                db_index=OrgApiKeyConstants.expiration_utc_date_time_calculatedIsDBColumnIndexed)
    is_active = models.BooleanField(
                                null=True,
                                db_column='is_active',
                                db_index=OrgApiKeyConstants.is_active_calculatedIsDBColumnIndexed)
    is_temp_user_key = models.BooleanField(
                                null=True,
                                db_column='is_temp_user_key',
                                db_index=OrgApiKeyConstants.is_temp_user_key_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_column='name',
                                db_index=OrgApiKeyConstants.name_calculatedIsDBColumnIndexed)
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization,
                               related_name='org_api_key_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='organization_id',
                               db_index=True)
    #org_customer_id = models.IntegerField(null=True)
    org_customer = models.ForeignKey(OrgCustomer,
                               related_name='org_api_key_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='org_customer_id',
                               db_index=True)
    objects = OrgApiKeyManager()
    class Meta:
        db_table = 'farm_org_api_key'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.org_api_key_id is not None:
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:OrgApiKey = OrgApiKey.objects.get(org_api_key_id=self.org_api_key_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.org_api_key_id is None:
            self.insert_utc_date_time = datetime.now(timezone.utc)
        self.last_update_utc_date_time = datetime.now(timezone.utc)
        self.last_change_code = uuid.uuid4()
        return super(OrgApiKey, self).save(*args, **kwargs)



    @staticmethod
    def build(organization:Organization
        ):
        item = OrgApiKey()
        item.code = uuid.uuid4()
        item.insert_utc_date_time = datetime.now(timezone.utc)
        item.last_update_utc_date_time = datetime.now(timezone.utc)
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.api_key_value = ""
        item.created_by = ""
        item.created_utc_date_time = TypeConversion.get_default_date_time()
        item.expiration_utc_date_time = TypeConversion.get_default_date_time()
        item.is_active = False
        item.is_temp_user_key = False
        item.name = ""
        item.organization = organization #organization_id
        item.org_customer = OrgCustomer.objects.from_enum(enum_val=OrgCustomerEnum.Unknown) #org_customer_id
        return item
    @staticmethod
    def initialize():
        pass

