from django.db import models
from enum import Enum 
import uuid

class DateGreaterThanFilterEnum(Enum):
    SWEET = 'Sweet'
    SOUR = 'Sour'
    UNKNOWN = 'Unknown'
    
class DateGreaterThanFilterManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code)
    
    def from_enum(self, enum_val:DateGreaterThanFilterEnum):
        return self.get(LookupEnumName=enum_val.value)
 