# models/mangers/date_greater_than_filter.py:
"""
This module defines the DateGreaterThanFilterManager class, 
which is responsible for
managing the DateGreaterThanFilter model.
"""
from enum import Enum
import uuid
from django.db import models

##GENTrainingBlock[caselookupenum]Start
##GENLearn[isLookup=true]Start
class DateGreaterThanFilterEnum(Enum):
    """
    This class defines the DateGreaterThanFilterEnum enumeration.
    """
    Last_24_Hours = 'Last_24_Hours'
    Last_7_Days = 'Last_7_Days'
    Last_30_Days = 'Last_30_Days'
    Last_90_Days = 'Last_90_Days'
    Last_365_Days = 'Last_365_Days'
    Unknown = 'Unknown'
##GENLearn[isLookup=true]End
##GENTrainingBlock[caselookupenum]End

class DateGreaterThanFilterManager(models.Manager):
    """
    This class is responsible for managing the
    DateGreaterThanFilter model.
    """

    def from_code(self, code: uuid.UUID):
        """
        This method returns the DateGreaterThanFilter object 
        with the specified code.
        """
        return self.get(code=code)

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true]Start
    def from_enum(self, enum_val:DateGreaterThanFilterEnum):
        """
        This method returns the DateGreaterThanFilter object
        with the specified enum value.
        """
        return self.get(lookup_enum_name=enum_val.value)
##GENLearn[isLookup=true]End
##GENTrainingBlock[caselookup]End
