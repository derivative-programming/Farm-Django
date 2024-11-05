# models/managers/plant.py
"""
This module defines the PlantManager class, which is responsible for managing Plant instances
"""
from enum import Enum
import uuid
from django.db import models

##GENTrainingBlock[caselookupenum]Start
##GENLearn[isLookup=false]Start
class PlantEnum(Enum):
    """
    Plant Enum
    """
##GENLearn[isLookup=false]End
##GENTrainingBlock[caselookupenum]End

class PlantManager(models.Manager):
    """
    Plant Manager
    """

    def from_code(self, code: uuid.UUID):
        """
        Get a Plant by code
        """
        return self.get(code=code)

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=false]Start
##GENLearn[isLookup=false]End
##GENTrainingBlock[caselookup]End
