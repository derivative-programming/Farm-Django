from django.db import models
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
import uuid
from .customer import Customer #customer_id
from .role import Role #role_id
import farm.models.constants.customer_role as CustomerRoleConstants
import logging
from farm.models.managers import CustomerManager,CustomerEnum #customer_id
from farm.models.managers import RoleManager,RoleEnum #role_id
from farm.models.managers import CustomerRoleManager,CustomerRoleEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class CustomerRole(models.Model):  
    customer_role_id = models.AutoField(primary_key=True,db_column='customer_role_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    #customer_id = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer,
                               related_name='customer_role_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='customer_id',
                               db_index=True)
    is_placeholder = models.BooleanField(
                                null=True,
                                db_column='is_placeholder',
                                db_index=CustomerRoleConstants.is_placeholder_calculatedIsDBColumnIndexed)
    placeholder = models.BooleanField(
                                null=True,
                                db_column='placeholder',
                                db_index=CustomerRoleConstants.placeholder_calculatedIsDBColumnIndexed)
    #role_id = models.IntegerField(null=True)
    role = models.ForeignKey(Role,
                               related_name='customer_role_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='role_id',
                               db_index=True)
    objects = CustomerRoleManager()
    class Meta:
        db_table = 'farm_customer_role'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.customer_role_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:CustomerRole = CustomerRole.objects.get(customer_role_id=self.customer_role_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.customer_role_id is None:
            self.insert_utc_date_time = datetime.now(timezone.utc)
        self.last_update_utc_date_time = datetime.now(timezone.utc)
        self.last_change_code = uuid.uuid4()
        return super(CustomerRole, self).save(*args, **kwargs)


   
    @staticmethod
    def build(customer:Customer
        ):
        item = CustomerRole()
        item.code = uuid.uuid4()
        item.insert_utc_date_time = datetime.now(timezone.utc)
        item.last_update_utc_date_time = datetime.now(timezone.utc)
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.customer = customer #customer_id
        item.is_placeholder = False
        item.placeholder = False
        item.role = Role.objects.from_enum(enum_val=RoleEnum.Unknown) #role_id
        return item
    @staticmethod
    def initialize():
        pass

