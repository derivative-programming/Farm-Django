# reports/providers/tests/__init__.py
"""
This module imports the tests for the report providers used in the project.
"""
##GENLOOPObjectStart
##GENTrainingBlock[a]Start
##GENLearn[modelType=object,name=Land]Start
##GENLOOPReportStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=report,name=LandPlantList]Start
from .land_plant_list import ReportProviderLandPlantListTest
##GENLearn[modelType=report,name=LandPlantList]End
##GENTrainingBlock[b]End
##GENLOOPReportEnd
##GENLearn[modelType=object,name=Land]End
from .tac_farm_dashboard import ReportProviderTacFarmDashboardTest
##GENTrainingBlock[a]End
##GENLOOPObjectEnd
