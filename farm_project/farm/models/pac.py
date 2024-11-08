from django.db import models
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
import uuid
import farm.models.constants.pac as PacConstants
from farm.models.managers import PacManager,PacEnum

class Pac(models.Model):
    pac_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4,db_index=True, unique=True)
    insert_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc))
    last_update_utc_date_time =models.DateTimeField(default=datetime.now(timezone.utc))
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    description = models.TextField(
                                null=True,
                                db_index=PacConstants.description_calculatedIsDBColumnIndexed)
    display_order = models.IntegerField(
                                null=True,
                                db_index=PacConstants.display_order_calculatedIsDBColumnIndexed)
    is_active = models.BooleanField(
                                null=True,
                                db_index=PacConstants.is_active_calculatedIsDBColumnIndexed)
    lookup_enum_name = models.TextField(
                                null=True,
                                db_index=PacConstants.lookup_enum_name_calculatedIsDBColumnIndexed)
    name = models.TextField(
                                null=True,
                                db_index=PacConstants.name_calculatedIsDBColumnIndexed)

    objects = PacManager()

    class Meta:
        db_table = 'farm_pac'
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
            self.insert_utc_date_time = datetime.now(timezone.utc)
        self.last_update_utc_date_time = datetime.now(timezone.utc)
        self.last_change_code = uuid.uuid4()
        return super(Pac, self).save(*args, **kwargs)

    def get_object_name(self):
        return "pac"

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=false]Start

    def get_parent_object(self):
        return None
    @staticmethod
    def build():
        item = Pac()
        item.description = ""
        item.display_order = 0
        item.code = uuid.uuid4()
        item.insert_utc_date_time = datetime.now(timezone.utc)
        item.last_update_utc_date_time = datetime.now(timezone.utc)
        item.insert_user_id = uuid.UUID(int=0)
        item.last_update_user_id = uuid.UUID(int=0)
        item.last_change_code = uuid.uuid4()
        item.is_active = False
        item.lookup_enum_name = ""
        item.name = ""
        return item
    @staticmethod
    def initialize():
        if Pac.objects.filter(lookup_enum_name=PacEnum.Unknown.value).exists() == False:
            item = Pac.build()
            item.code = uuid.uuid4()
            item.name = "Unknown" #vrdebug
            item.lookup_enum_name = "Unknown"
            item.description = "Unknown"
            item.display_order = 1
            item.is_active = True
            item.save()
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=false]End
##GENTrainingBlock[caselookup]End
