from django.db import models
from enum import Enum 
import uuid

##GENTrainingBlock[caselookupenum]Start
##GENLearn[isLookup=true]Start
class FlavorEnum(Enum):
    SWEET = 'Sweet'
    SOUR = 'Sour'
    UNKNOWN = 'Unknown'
##GENLearn[isLookup=true]End
##GENTrainingBlock[caselookupenum]End
    
class FlavorManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code) 
    
 
##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true]Start
    def from_enum(self, enum_val:FlavorEnum):
        return self.get(LookupEnumName=enum_val.value)
##GENLearn[isLookup=true]End
##GENTrainingBlock[caselookup]End