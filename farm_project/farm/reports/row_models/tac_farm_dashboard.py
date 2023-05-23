from dataclasses import dataclass
import uuid 

@dataclass
class ReportItemTacFarmDashboard():
    field_one_plant_list_link_land_code:uuid = uuid.UUID(int=0)

    def __init__(self): 
        pass
 

    def load_data_provider_dict(self,data:dict):
            self.field_one_plant_list_link_land_code = uuid.UUID(data["field_one_plant_list_link_land_code"])