from django.db import models
from enum import Enum 
import uuid 

class TriStateFilterEnum(Enum):
    SWEET = 'Sweet'
    SOUR = 'Sour'
    UNKNOWN = 'Unknown'
    
class TriStateFilterManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code)
    
    def from_enum(self, enum_val:TriStateFilterEnum):
        return self.get(LookupEnumName=enum_val.value)