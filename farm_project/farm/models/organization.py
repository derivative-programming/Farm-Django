from django.db import models
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
import uuid
from .tac import Tac #tac_id
import farm.models.constants.organization as OrganizationConstants
import logging
from farm.models.managers import TacManager,TacEnum #tac_id
from farm.models.managers import OrganizationManager,OrganizationEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class Organization(models.Model):  
    organization_id = models.AutoField(primary_key=True,db_column='organization_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc),db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    name = models.TextField(
                                null=True,
                                db_column='name',
                                db_index=OrganizationConstants.name_calculatedIsDBColumnIndexed)
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac,
                               related_name='organization_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='tac_id',
                               db_index=True)
    objects = OrganizationManager()
    class Meta:
        db_table = 'farm_organization'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.organization_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:Organization = Organization.objects.get(organization_id=self.organization_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.organization_id is None:
            self.insert_utc_date_time = datetime.now(timezone.utc)
        self.last_update_utc_date_time = datetime.now(timezone.utc)
        self.last_change_code = uuid.uuid4()
        return super(Organization, self).save(*args, **kwargs)


   
    @staticmethod
    def build(tac:Tac
        ):
        item = Organization()
        item.code = uuid.uuid4()
        item.insert_utc_date_time = datetime.now(timezone.utc)
        item.last_update_utc_date_time = datetime.now(timezone.utc)
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.name = ""
        item.tac = tac #tac_id
        return item
    @staticmethod
    def initialize():
        pass

