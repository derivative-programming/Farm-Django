from django.db import models
from enum import Enum 
import uuid  
    
##GENTrainingBlock[caselookupenum]Start
##GENLearn[isLookup=false]Start
##GENLearn[isLookup=false]End
##GENTrainingBlock[caselookupenum]End

class PlantManager(models.Manager):

    def from_code(self, code:uuid):
        return self.get(code=code)
    
##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=false]Start
##GENLearn[isLookup=false]End
##GENTrainingBlock[caselookup]End