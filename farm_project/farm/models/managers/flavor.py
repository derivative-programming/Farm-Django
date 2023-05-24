from django.db import models
from enum import Enum 
import uuid

class FlavorEnum(Enum):
    SWEET = 'Sweet'
    SOUR = 'Sour'
    UNKNOWN = 'Unknown'
    
class FlavorManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code) 
    
 
    def from_enum(self, enum_val:FlavorEnum):
        return self.get(LookupEnumName=enum_val.value)