from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .organization import Organization #organization_id
from .org_customer import OrgCustomer #org_customer_id
import api.models.constants.org_api_key as OrgApiKeyConstants
class OrgApiKey(models.Model):  
    org_api_key_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True, unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    api_key_value = models.TextField(
                                null=True,
                                db_index=OrgApiKeyConstants.api_key_value_calculatedIsDBColumnIndexed)
    created_by = models.TextField(
                                null=True,
                                db_index=OrgApiKeyConstants.created_by_calculatedIsDBColumnIndexed)
    created_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=OrgApiKeyConstants.created_utc_date_time_calculatedIsDBColumnIndexed)
    expiration_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=OrgApiKeyConstants.expiration_utc_date_time_calculatedIsDBColumnIndexed)
    is_active = models.BooleanField(
                                null=True,
                                db_index=OrgApiKeyConstants.is_active_calculatedIsDBColumnIndexed)
    is_temp_user_key = models.BooleanField(
                                null=True,
                                db_index=OrgApiKeyConstants.is_temp_user_key_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_index=OrgApiKeyConstants.name_calculatedIsDBColumnIndexed)
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization,
                               related_name='org_api_key_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_index=True)
    #org_customer_id = models.IntegerField(null=True)
    org_customer = models.ForeignKey(OrgCustomer,
                               related_name='org_api_key_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_index=True)
    class Meta:
        db_table = 'farm_org_api_key'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.org_api_key_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance = OrgApiKey.objects.get(org_api_key_id=self.org_api_key_id)
            if self.last_change_code != current_instance.last_change_code:
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.org_api_key_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(OrgApiKey, self).save(*args, **kwargs)
