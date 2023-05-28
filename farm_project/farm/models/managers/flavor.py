from django.db import models
from enum import Enum 
import uuid  
 
class FlavorEnum(Enum):
    Unknown = 'Unknown'
    Sweet = 'Sweet'
    Sour = 'Sour'


class FlavorManager(models.Manager):
    def from_code(self, code:uuid):
        return self.get(code=code)

    def from_enum(self, enum_val:FlavorEnum):
        return self.get(lookup_enum_name=enum_val.value)


