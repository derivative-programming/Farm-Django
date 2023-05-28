from django.db import models
from enum import Enum 
import uuid  
 
class LandEnum(Enum):
    Unknown = 'Unknown'
    Field_One = 'Field_One'


class LandManager(models.Manager):
    def from_code(self, code:uuid):
        return self.get(code=code)

    def from_enum(self, enum_val:LandEnum):
        return self.get(lookup_enum_name=enum_val.value)


