# views/factories/__init__.py
"""
This module imports the factories used in the project.
"""
##GENLOOPObjectStart
##GENTrainingBlock[a]Start
##GENLearn[modelType=object,name=Land]Start
##GENLOOPObjectWorkflowStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=objectWorkflow,name=LandAddPlant,calculatedIsInitObjWF=false]Start
from .land_add_plant import LandAddPlantPostModelRequestFactory
##GENLearn[modelType=objectWorkflow,name=LandAddPlant,calculatedIsInitObjWF=false]End
##GENTrainingBlock[b]End
##GENLOOPObjectWorkflowEnd
##GENLearn[modelType=object,name=Land]End
##GENTrainingBlock[a]End
##GENLOOPObjectEnd

##GENLOOPObjectStart
##GENTrainingBlock[a2]Start
##GENLearn[modelType=object,name=Land]Start
##GENLOOPReportStart
##GENTrainingBlock[b2]Start
##GENLearn[modelType=report,name=LandPlantList]Start
from .land_plant_list import LandPlantListGetModelRequestFactory
##GENLearn[modelType=report,name=LandPlantList]End
##GENTrainingBlock[b2]End
##GENLOOPReportEnd
##GENLearn[modelType=object,name=Land]End
##GENTrainingBlock[a2]End
##GENLOOPObjectEnd
