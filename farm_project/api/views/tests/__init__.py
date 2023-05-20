
##GENLOOPObjectStart
##GENTrainingBlock[a]Start
##GENLearn[modelType=object,name=Tac]Start 
##GENLOOPObjectWorkflowStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=objectWorkflow,name=TacRegister]Start 
from .land_add_plant import LandAddPlantViewSetTestCase
##GENLearn[modelType=objectWorkflow,name=TacRegister]End
##GENTrainingBlock[b]End
##GENLOOPObjectWorkflowEnd
##GENLearn[modelType=object,name=Tac]End 
from .tac_login import TacLoginViewSetTestCase
from .tac_register import TacRegisterViewSetTestCase
##GENTrainingBlock[a]End
##GENLOOPObjectEnd

##GENLOOPObjectStart
##GENTrainingBlock[a2]Start
##GENLearn[modelType=object,name=Tac]Start 
##GENLOOPReportStart
##GENTrainingBlock[b2]Start
##GENLearn[modelType=report,name=TacFarmDashboard]Start 
from .land_plant_list import LandPlantListViewSetTestCase
##GENLearn[modelType=report,name=TacFarmDashboard]End
##GENTrainingBlock[b2]End
##GENLOOPReportEnd
##GENLearn[modelType=object,name=Tac]End  
from .tac_farm_dashboard import TacFarmDashboardViewSetTestCase
##GENTrainingBlock[a2]End
##GENLOOPObjectEnd