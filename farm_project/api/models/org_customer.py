from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .customer import Customer #customer_id
from .organization import Organization #organization_id
import api.models.constants.org_customer as OrgCustomerConstants
class OrgCustomer(models.Model):  
    org_customer_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #customer_id = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer,
                               related_name='org_customer_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_index=True)
    email = models.TextField(
                                max_length=50,
                                null=True,
                                db_index=OrgCustomerConstants.email_calculatedIsDBColumnIndexed)
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization,
                               related_name='org_customer_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_index=True)
    class Meta:
        db_table = 'farm_org_customer'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.org_customer_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance = OrgCustomer.objects.get(org_customer_id=self.org_customer_id)
            if self.last_change_code != current_instance.last_change_code:
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.org_customer_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(OrgCustomer, self).save(*args, **kwargs)
