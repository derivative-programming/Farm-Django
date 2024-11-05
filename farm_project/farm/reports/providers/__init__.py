##GENLOOPObjectStart
##GENTrainingBlock[a]Start
##GENLearn[modelType=object,name=Land]Start
##GENLOOPReportStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=report,name=LandPlantList]Start
from .land_plant_list import ReportProviderLandPlantList
##GENLearn[modelType=report,name=LandPlantList]End
##GENTrainingBlock[b]End
##GENLOOPReportEnd
##GENLearn[modelType=object,name=Land]End
from .tac_farm_dashboard import ReportProviderTacFarmDashboard
##GENTrainingBlock[a]End
##GENLOOPObjectEnd
