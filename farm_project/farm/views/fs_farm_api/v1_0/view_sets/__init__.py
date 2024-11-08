# views/fs_farm_api/v1_0/view_sets/__init__.py
"""
This module initializes the view sets used in the project.
"""
##GENLOOPApiEndPointStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=apiEndPoint,name=LandAddPlant]Start
from .land_add_plant import LandAddPlantViewSet
##GENLearn[modelType=apiEndPoint,name=LandAddPlant]End
from .tac_login import TacLoginViewSet
from .tac_register import TacRegisterViewSet
from .land_plant_list import LandPlantListViewSet
from .tac_farm_dashboard import TacFarmDashboardViewSet
##GENTrainingBlock[b]End
##GENLOOPApiEndPointEnd
