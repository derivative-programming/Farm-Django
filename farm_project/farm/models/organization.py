from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .tac import Tac #tac_id
import farm.models.constants.organization as OrganizationConstants
from farm.models.managers import OrganizationManager

class Organization(models.Model):  
    organization_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True, unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    name = models.TextField(
                                null=True,
                                db_index=OrganizationConstants.name_calculatedIsDBColumnIndexed)
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac,
                               related_name='organization_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
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
            current_instance = Organization.objects.get(organization_id=self.organization_id)
            if self.last_change_code != current_instance.last_change_code:
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.organization_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Organization, self).save(*args, **kwargs)


    @staticmethod
    def initialize():
        pass