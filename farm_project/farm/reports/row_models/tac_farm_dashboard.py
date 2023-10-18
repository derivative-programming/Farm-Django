from dataclasses import dataclass, field
from dataclasses_json import config
from datetime import date, datetime
import uuid
from decimal import Decimal
from farm.helpers import TypeConversion
@dataclass
class ReportItemTacFarmDashboard():
    field_one_plant_list_link_land_code:uuid = uuid.UUID(int=0)
    conditional_btn_example_link_land_code:uuid = uuid.UUID(int=0)
    is_conditional_btn_available:bool = False
#endset
    def __init__(self): 
        pass
    def load_data_provider_dict(self,data:dict):
            self.field_one_plant_list_link_land_code = uuid.UUID(data["field_one_plant_list_link_land_code"])
            self.conditional_btn_example_link_land_code = uuid.UUID(data["conditional_btn_example_link_land_code"])
            self.is_conditional_btn_available = bool(data["is_conditional_btn_available"])

