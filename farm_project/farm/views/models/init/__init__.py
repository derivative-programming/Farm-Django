##GENLOOPObjectStart
##GENTrainingBlock[a]Start
##GENLearn[modelType=object,name=Land]Start
##GENLOOPObjectWorkflowStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=objectWorkflow,name=LandAddPlantInitObjWF,calculatedIsInitObjWF=true]Start
from .land_add_plant_init_obj_wf import LandAddPlantInitObjWFGetInitModelRequest, LandAddPlantInitObjWFGetInitModelResponse
##GENLearn[modelType=objectWorkflow,name=LandAddPlantInitObjWF,calculatedIsInitObjWF=true]End
##GENTrainingBlock[b]End
##GENLOOPObjectWorkflowEnd
##GENLearn[modelType=object,name=Land]End
from .land_plant_list_init_report import LandPlantListInitReportGetInitModelRequest,LandPlantListInitReportGetInitModelResponse
from .tac_farm_dashboard_init_report import TacFarmDashboardInitReportGetInitModelRequest, TacFarmDashboardInitReportGetInitModelResponse
from .tac_login_init_obj_wf import TacLoginInitObjWFGetInitModelRequest, TacLoginInitObjWFGetInitModelResponse
from .tac_register_init_obj_wf import TacRegisterInitObjWFGetInitModelRequest, TacRegisterInitObjWFGetInitModelResponse
##GENTrainingBlock[a]End
##GENLOOPObjectEnd
