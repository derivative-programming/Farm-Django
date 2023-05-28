from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .pac import Pac #pac_id
import farm.models.constants.role as RoleConstants
import logging
from farm.models.managers import PacManager,PacEnum #pac_id
from farm.models.managers import RoleManager,RoleEnum
from decimal import Decimal
from farm.helpers import TypeConversion
class Role(models.Model):  
    role_id = models.AutoField(primary_key=True,db_column='role_id')
    code = models.UUIDField(default=uuid.uuid4,db_index=True,db_column='code', unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now,db_column='insert_utc_date_time')
    last_update_utc_date_time =models.DateTimeField(default=timezone.now,db_column='last_update_utc_date_time')
    insert_user_id = models.UUIDField(null=True,db_column='insert_user_id')
    last_update_user_id = models.UUIDField(null=True,db_column='last_update_user_id')
    last_change_code = models.UUIDField(default=uuid.uuid4,db_column='last_change_code')	
    description = models.TextField(
                                null=True,
                                db_column='description',
                                db_index=RoleConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_column='display_order',
                                db_index=RoleConstants.display_order_calculatedIsDBColumnIndexed)	
    is_active = models.BooleanField(
                                null=True,
                                db_column='is_active',
                                db_index=RoleConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_column='lookup_enum_name',
                                db_index=RoleConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_column='name',
                                db_index=RoleConstants.name_calculatedIsDBColumnIndexed)
    #pac_id = models.IntegerField(null=True)
    pac = models.ForeignKey(Pac,
                               related_name='role_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_column='pac_id',
                               db_index=True)
    objects = RoleManager()
    class Meta:
        db_table = 'farm_role'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.role_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance:Role = Role.objects.get(role_id=self.role_id)
            if self.last_change_code != current_instance.last_change_code:
                logging.debug("in db: " + str(current_instance.last_change_code) + " yours: " + str(self.last_change_code))
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.role_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Role, self).save(*args, **kwargs)
  #vrdebug
    @staticmethod
    def build(pac:Pac
        ):
        item = Role()
        item.description = ""
        item.display_order = 0
        item.code = uuid.uuid4()
        item.insert_utc_date_time = timezone.now
        item.last_update_utc_date_time = timezone.now
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.is_active = False
        item.lookupEnumName = ""
        item.name = ""
        #pac_id = models.IntegerField(null=True)
        item.pac = pac
        return item
    @staticmethod
    def initialize():
        pac = Pac.objects.all().first()
        if Role.objects.filter(lookup_enum_name=RoleEnum.Unknown.value).exists() == False:
            item = Role.build(pac)
            item.name = ""
            item.lookup_enum_name = "Unknown"
            item.description = ""
            item.display_order = Role.objects.count()
            item.is_active = True
            # item. = 1
            item.save()
        if Role.objects.filter(lookup_enum_name=RoleEnum.Admin.value).exists() == False:
            item = Role.build(pac)
            item.name = "Admin"
            item.lookup_enum_name = "Admin"
            item.description = "Admin"
            item.display_order = Role.objects.count()
            item.is_active = True
            # item. = 1
            item.save()
        if Role.objects.filter(lookup_enum_name=RoleEnum.Config.value).exists() == False:
            item = Role.build(pac)
            item.name = "Config"
            item.lookup_enum_name = "Config"
            item.description = "Config"
            item.display_order = Role.objects.count()
            item.is_active = True
            # item. = 1
            item.save()
        if Role.objects.filter(lookup_enum_name=RoleEnum.User.value).exists() == False:
            item = Role.build(pac)
            item.name = "User"
            item.lookup_enum_name = "User"
            item.description = "User"
            item.display_order = Role.objects.count()
            item.is_active = True
            # item. = 1
            item.save()



