from django.db import models
from enum import Enum 
import uuid

class LandEnum(Enum):
    SWEET = 'Sweet'
    SOUR = 'Sour'
    UNKNOWN = 'Unknown'
    
class LandManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code)
    
    def from_enum(self, enum_val:LandEnum):
        return self.get(LookupEnumName=enum_val.value)