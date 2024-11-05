from django.db import models
from enum import Enum
import uuid


class CustomerRoleEnum(Enum):
    pass

class CustomerRoleManager(models.Manager):
    def from_code(self, code: uuid.UUID):
        return self.get(code=code)



