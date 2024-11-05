# views/fs_farm_api/v1_0/tests/__init__.py
"""
This module imports all of the test view sets used in the project.
"""
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
