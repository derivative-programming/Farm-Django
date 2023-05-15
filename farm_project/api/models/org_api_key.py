from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .organization import Organization #organization_id
from .org_customer import OrgCustomer #org_customer_id
from api.models.constants import OrgApiKeyConstants
class OrgApiKey(models.Model): 
    org_api_keyConstants = OrgApiKeyConstants()
    org_api_key_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    api_key_value = models.TextField(
                                null=True,
                                db_index=org_api_keyConstants.api_key_value_calculatedIsDBColumnIndexed)
    created_by = models.TextField(
                                null=True,
                                db_index=org_api_keyConstants.created_by_calculatedIsDBColumnIndexed)
    created_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=org_api_keyConstants.created_utc_date_time_calculatedIsDBColumnIndexed)
    expiration_utc_date_time = models.DateTimeField(
                                null=True,
                                db_index=org_api_keyConstants.expiration_utc_date_time_calculatedIsDBColumnIndexed)
    is_active = models.BooleanField(
                                null=True,
                                db_index=org_api_keyConstants.is_active_calculatedIsDBColumnIndexed)
    is_temp_user_key = models.BooleanField(
                                null=True,
                                db_index=org_api_keyConstants.is_temp_user_key_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_index=org_api_keyConstants.name_calculatedIsDBColumnIndexed)
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
