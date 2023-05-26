from django.db import models
from enum import Enum
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid
from .pac import Pac #pac_id
import farm.models.constants.flavor as FlavorConstants 
from farm.models.managers import FlavorManager,FlavorEnum
 

class Flavor(models.Model):  
    flavor_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True, unique=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    description = models.TextField(
                                null=True,
                                db_index=FlavorConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_index=FlavorConstants.display_order_calculatedIsDBColumnIndexed)	
    is_active = models.BooleanField(
                                null=True,
                                db_index=FlavorConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_index=FlavorConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_index=FlavorConstants.name_calculatedIsDBColumnIndexed)
    #pac_id = models.IntegerField(null=True)
    pac = models.ForeignKey(Pac,
                               related_name='flavor_list',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               db_index=True)
        
    objects = FlavorManager()

    class Meta:
        db_table = 'farm_flavor'
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.flavor_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance = Flavor.objects.get(flavor_id=self.flavor_id)
            if self.last_change_code != current_instance.last_change_code:
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.flavor_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Flavor, self).save(*args, **kwargs)


    @staticmethod
    def initialize():
        pac = Pac.objects.all().first()
        if Flavor.objects.filter(lookup_enum_name=FlavorEnum.Sour.value).exists() == False:
            item = Flavor() 
            item.pac = pac
            item.code = uuid.uuid4()
            item.name = "Sour"
            item.lookup_enum_name = "Sour"
            item.description = "Sour"
            item.display_order = Flavor.objects.count()
            item.is_active = True 
            item.save()
        if Flavor.objects.filter(lookup_enum_name=FlavorEnum.Sweet.value).exists() == False:
            item = Flavor() 
            item.pac = pac
            item.code = uuid.uuid4()
            item.name = "Sweet"
            item.lookup_enum_name = "Sweet"
            item.description = "Sweet"
            item.display_order = Flavor.objects.count()
            item.is_active = True 
            item.save()
        if Flavor.objects.filter(lookup_enum_name=FlavorEnum.Unknown.value).exists() == False:
            item = Flavor() 
            item.pac = pac
            item.code = uuid.uuid4()
            item.name = "Unknown"
            item.lookup_enum_name = "Unknown"
            item.description = "Unknown"
            item.display_order = Flavor.objects.count()
            item.is_active = True 
            item.save()