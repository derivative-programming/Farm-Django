
##GENLOOPObjectStart
##GENTrainingBlock[a]Start
##GENLearn[modelType=object,name=Tac]Start 
##GENLOOPObjectWorkflowStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=objectWorkflow,name=TacRegister]Start 
from .tac_register import TacRegisterViewSetTestCase
##GENLearn[modelType=objectWorkflow,name=TacRegister]End
##GENTrainingBlock[b]End
##GENLOOPObjectWorkflowEnd
##GENLearn[modelType=object,name=Tac]End 
from .tac_login import TacLoginViewSetTestCase
from .land_add_plant import LandAddPlantViewSetTestCase
##GENTrainingBlock[a]End
##GENLOOPObjectEnd

##GENLOOPObjectStart
##GENTrainingBlock[a2]Start
##GENLearn[modelType=object,name=Tac]Start 
##GENLOOPReportStart
##GENTrainingBlock[b2]Start
##GENLearn[modelType=report,name=TacFarmDashboard]Start 
from .tac_farm_dashboard import TacFarmDashboardViewSetTestCase
##GENLearn[modelType=report,name=TacFarmDashboard]End
##GENTrainingBlock[b2]End
##GENLOOPReportEnd
##GENLearn[modelType=object,name=Tac]End  
from .land_plant_list import LandPlantListViewSetTestCase
##GENTrainingBlock[a2]End
##GENLOOPObjectEnd