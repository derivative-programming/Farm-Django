from django.db import models
from enum import Enum
import uuid


class OrgApiKeyEnum(Enum):
    pass

class OrgApiKeyManager(models.Manager):
    def from_code(self, code: uuid.UUID):
        return self.get(code=code)



