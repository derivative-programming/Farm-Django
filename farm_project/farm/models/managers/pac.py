from django.db import models
from enum import Enum
import uuid

class PacEnum(Enum):
    Unknown = 'Unknown'


class PacManager(models.Manager):
    def from_code(self, code: uuid.UUID):
        return self.get(code=code)

    def from_enum(self, enum_val:PacEnum):
        return self.get(lookup_enum_name=enum_val.value)


