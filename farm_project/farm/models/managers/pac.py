from django.db import models
from enum import Enum 
import uuid 

class PacEnum(Enum):
    SWEET = 'Sweet'
    SOUR = 'Sour'
    UNKNOWN = 'Unknown'
    
class PacManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code)
    
    def from_enum(self, enum_val:PacEnum):
        return self.get(LookupEnumName=enum_val.value)