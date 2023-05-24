from django.db import models
from enum import Enum 
import uuid

##GENTrainingBlock[caselookupenum]Start
##GENLearn[isLookup=true]Start 
class DateGreaterThanFilterEnum(Enum):
    Last_24_Hours = 'Last_24_Hours'
    Last_7_Days = 'Last_7_Days'
    Last_30_Days = 'Last_30_Days'
    Last_90_Days = 'Last_90_Days'
    Last_365_Days = 'Last_365_Days'
    Unknown = 'Unknown'
##GENLearn[isLookup=true]End
##GENTrainingBlock[caselookupenum]End
    
class DateGreaterThanFilterManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code)
    
##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true]Start
    def from_enum(self, enum_val:DateGreaterThanFilterEnum):
        return self.get(LookupEnumName=enum_val.value)
##GENLearn[isLookup=true]End
##GENTrainingBlock[caselookup]End