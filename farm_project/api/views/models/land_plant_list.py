from dataclasses import dataclass, field 
from dataclasses_json import dataclass_json, LetterCase, config
from typing import List
from datetime import date, datetime
import uuid
from decimal import Decimal
from api.helpers import TypeConversion
from api.reports.row_models import ReportItemLandPlantList 
from api.views.models import ListRequest, ListModel 
   


### request. expect camel case. use marshmallow to validate.
@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class LandPlantListListRequest(ListRequest):
    pass 

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandPlantListListModelItem():
    plant_code:uuid = uuid.UUID(int=0)
    some_int_val:int = 0 
    some_big_int_val:int = 0 
    some_bit_val:bool = False 
    is_edit_allowed:bool = False 
    is_delete_allowed:bool = False 
    some_float_val:float = 0
    some_decimal_val:Decimal = Decimal(0)
    some_utc_date_time_val:datetime = field(default_factory=TypeConversion.get_default_date_time, 
            metadata=config(
            encoder=datetime.isoformat, 
            decoder=datetime.fromisoformat
        )) 
    some_date_val:date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat, 
            decoder=date.fromisoformat
        ))
    some_money_val:Decimal = Decimal(0)
    some_n_var_char_val:str = "" 
    some_var_char_val:str = "" 
    some_text_val:str = "" 
    some_phone_number:str = "" 
    some_email_address:str = "" 
    flavor_name:str = "" 
    flavor_code:uuid = uuid.UUID(int=0)
    some_int_conditional_on_deletable:int = 0 
    n_var_char_as_url:str = "" 
    update_link_plant_code:uuid = uuid.UUID(int=0)
    delete_async_button_link_plant_code:uuid = uuid.UUID(int=0)
    details_link_plant_code:uuid = uuid.UUID(int=0)
#endset

    def load_report_item(self,data:ReportItemLandPlantList): 
        self.plant_code = data.plant_code
        self.some_int_val = data.some_int_val
        self.some_big_int_val = data.some_big_int_val
        self.some_bit_val = data.some_bit_val
        self.is_edit_allowed = data.is_edit_allowed
        self.is_delete_allowed = data.is_delete_allowed
        self.some_float_val = data.some_float_val
        self.some_decimal_val = data.some_decimal_val
        self.some_utc_date_time_val = data.some_utc_date_time_val
        self.some_date_val = data.some_date_val
        self.some_money_val = data.some_money_val
        self.some_n_var_char_val = data.some_n_var_char_val
        self.some_var_char_val = data.some_var_char_val
        self.some_text_val = data.some_text_val
        self.some_phone_number = data.some_phone_number
        self.some_email_address = data.some_email_address
        self.flavor_name = data.flavor_name
        self.flavor_code = data.flavor_code
        self.some_int_conditional_on_deletable = data.some_int_conditional_on_deletable
        self.n_var_char_as_url = data.n_var_char_as_url
        self.update_link_plant_code = data.update_link_plant_code
        self.delete_async_button_link_plant_code = data.delete_async_button_link_plant_code
        self.details_link_plant_code = data.details_link_plant_code
#endset


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandPlantListListModel(ListModel):
    request:LandPlantListListRequest = None
    items:List[LandPlantListListModelItem] = field(default_factory=list)
   