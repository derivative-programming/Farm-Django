from django.db import models
from enum import Enum 
import uuid  
 
class TriStateFilterEnum(Enum):
    Unknown = 'Unknown'
    Yes = 'Yes'
    No = 'No'


class TriStateFilterManager(models.Manager):
    def from_code(self, code:uuid):
        return self.get(code=code)

    def from_enum(self, enum_val:TriStateFilterEnum):
        return self.get(lookup_enum_name=enum_val.value)


