from django.db import models
from enum import Enum 
import uuid  
 
class TacEnum(Enum):
    Unknown = 'Unknown'
    Primary = 'Primary'


class TacManager(models.Manager):
    def from_code(self, code:uuid):
        return self.get(code=code)

    def from_enum(self, enum_val:TacEnum):
        return self.get(LookupEnumName=enum_val.value)
 

