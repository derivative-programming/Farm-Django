from django.db import models
from enum import Enum 
import uuid 
    
class OrgApiKeyManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code)
    