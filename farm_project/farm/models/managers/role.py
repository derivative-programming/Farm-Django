from django.db import models
from enum import Enum 
import uuid  
 
class RoleEnum(Enum):
    Unknown = 'Unknown'
    Admin = 'Admin'
    Config = 'Config'
    User = 'User'


class RoleManager(models.Manager):
    def from_code(self, code:uuid):
        return self.get(code=code)

    def from_enum(self, enum_val:RoleEnum):
        return self.get(LookupEnumName=enum_val.value)
 