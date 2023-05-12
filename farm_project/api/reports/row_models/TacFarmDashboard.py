from dataclasses import dataclass
import uuid 

@dataclass
class ReportItemTacFarmDashboard():
    field_one_land_plant_list_link_plant_code:uuid = uuid.UUID(int=0)

    def __init__(self): 
        pass
 
