from django.db import models
from enum import Enum
import uuid


class OrganizationEnum(Enum):
    pass

class OrganizationManager(models.Manager):
    def from_code(self, code: uuid.UUID):
        return self.get(code=code)



