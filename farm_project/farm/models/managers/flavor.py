from django.db import models
from enum import Enum 
import uuid  
import logging
 
class FlavorEnum(Enum):
    Unknown = 'Unknown'
    Sweet = 'Sweet'
    Sour = 'Sour'


class FlavorManager(models.Manager):
    def from_code(self, code:uuid): 
        logging.debug(self.all()) 
        return self.get(code=code)

    def from_enum(self, enum_val:FlavorEnum):  
        logging.debug(self.all().first().lookup_enum_name) 
        return self.get(lookup_enum_name=enum_val.value)


