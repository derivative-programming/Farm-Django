##GENLOOPapiEndPointStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=apiEndPoint,name=LandAddPlant]Start
from .land_add_plant import LandAddPlantViewSetTestCase
##GENLearn[modelType=apiEndPoint,name=LandAddPlant]End
from .tac_login import TacLoginViewSetTestCase
from .tac_register import TacRegisterViewSetTestCase
from .land_plant_list import LandPlantListViewSetTestCase
from .tac_farm_dashboard import TacFarmDashboardViewSetTestCase
##GENTrainingBlock[b]End
##GENLOOPapiEndPointEnd
