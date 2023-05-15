from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import uuid 

from api.models.constants import PacConstants
class Pac(models.Model): 
    pacConstants = PacConstants()
    pac_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_update_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    description = models.TextField(
                                null=True,
                                db_index=pacConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_index=pacConstants.display_order_calculatedIsDBColumnIndexed)	
    is_active = models.BooleanField(
                                null=True,
                                db_index=pacConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_index=pacConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_index=pacConstants.name_calculatedIsDBColumnIndexed)
    def __str__(self):
        return str(self.code)
    def save(self, *args, **kwargs):
       # On save, update timestamps
        if self.pac_id is not None:  
            # If the instance already exists in the database, make sure it hasn't already changed since last read
            current_instance = Pac.objects.get(pac_id=self.pac_id)
            if self.last_change_code != current_instance.last_change_code:
                raise ValidationError('This object is invalid. It has already changed in the db.')
        if self.pac_id is None:
            self.insert_utc_date_time = timezone.now()
        self.last_update_utc_date_time = timezone.now()
        self.last_change_code = uuid.uuid4()
        return super(Pac, self).save(*args, **kwargs)
