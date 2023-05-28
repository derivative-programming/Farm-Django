from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .customer import Customer #customer_id
from .organization import Organization #organization_id
import farm.models.constants.org_customer as OrgCustomerConstants
import logging
from farm.models.managers import CustomerManager,CustomerEnum #customer_id
from farm.models.managers import OrganizationManager,OrganizationEnum #organization_id
from farm.models.managers import OrgCustomerManager,OrgCustomerEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class OrgCustomer(models.Model):  
    org_customer_id = models.AutoField(primary_key=True,db_column='org_customer_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now,db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=timezone.now,db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    #customer_id = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer,
                               related_name='org_customer_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='customer_id',
                               db_index=True)
    email = models.TextField(
                                max_length=50,
                                null=True,
                                db_column='email',
                                db_index=OrgCustomerConstants.email_calculatedIsDBColumnIndexed)
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization,
                               related_name='org_customer_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='organization_id',
                               db_index=True)
    objects = OrgCustomerManager()
    class Meta:
        db_table = 'farm_org_customer'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.org_customer_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:OrgCustomer = OrgCustomer.objects.get(org_customer_id=self.org_customer_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.org_customer_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(OrgCustomer, self).save(*args, **kwargs)


   
    @staticmethod
    def build(organization:Organization
        ):
        item = OrgCustomer()
        item.code = uuid.uuid4()
        item.insert_utc_date_time = timezone.now
        item.last_update_utc_date_time = timezone.now
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.customer = Customer.objects.from_enum(enum_val=CustomerEnum.Unknown) #customer_id
        item.email = ""
        item.organization = organization #organization_id
        return item
    @staticmethod
    def initialize():
        pass

