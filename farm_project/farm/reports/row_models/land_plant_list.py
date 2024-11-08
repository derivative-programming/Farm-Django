from dataclasses import dataclass, field
from dataclasses_json import config
from datetime import date, datetime
import uuid
from decimal import Decimal
from farm.helpers import TypeConversion
@dataclass
class ReportItemLandPlantList():
    plant_code: uuid.UUID = uuid.UUID(int=0)
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
    flavor_code: uuid.UUID = uuid.UUID(int=0)
    some_int_conditional_on_deletable:int = 0
    n_var_char_as_url:str = ""
    update_link_plant_code: uuid.UUID = uuid.UUID(int=0)
    delete_async_button_link_plant_code: uuid.UUID = uuid.UUID(int=0)
    details_link_plant_code: uuid.UUID = uuid.UUID(int=0)
    test_file_download_link_pac_code: uuid.UUID = uuid.UUID(int=0)
    test_conditional_file_download_link_pac_code: uuid.UUID = uuid.UUID(int=0)
    test_async_flow_req_link_pac_code: uuid.UUID = uuid.UUID(int=0)
    test_conditional_async_flow_req_link_pac_code: uuid.UUID = uuid.UUID(int=0)
    conditional_btn_example_link_plant_code: uuid.UUID = uuid.UUID(int=0)
#endset
    def __init__(self):
        pass
    def load_data_provider_dict(self,data:dict):
            self.plant_code = uuid.UUID(data["plant_code"])
            self.some_int_val = int(data["some_int_val"])
            self.some_big_int_val = int(data["some_big_int_val"])
            self.some_bit_val = bool(data["some_bit_val"])
            self.is_edit_allowed = bool(data["is_edit_allowed"])
            self.is_delete_allowed = bool(data["is_delete_allowed"])
            self.some_float_val = float(data["some_float_val"])
            self.some_decimal_val = Decimal(data["some_decimal_val"])
            self.some_utc_date_time_val = datetime(data["some_utc_date_time_val"])
            self.some_date_val = date(data["some_date_val"])
            self.some_money_val = Decimal(data["some_money_val"])
            self.some_n_var_char_val = str(data["some_n_var_char_val"])
            self.some_var_char_val = str(data["some_var_char_val"])
            self.some_text_val = str(data["some_text_val"])
            self.some_phone_number = str(data["some_phone_number"])
            self.some_email_address = str(data["some_email_address"])
            self.flavor_name = str(data["flavor_name"])
            self.flavor_code = uuid.UUID(data["flavor_code"])
            self.some_int_conditional_on_deletable = int(data["some_int_conditional_on_deletable"])
            self.n_var_char_as_url = str(data["n_var_char_as_url"])
            self.update_link_plant_code = uuid.UUID(data["update_link_plant_code"])
            self.delete_async_button_link_plant_code = uuid.UUID(data["delete_async_button_link_plant_code"])
            self.details_link_plant_code = uuid.UUID(data["details_link_plant_code"])
            self.test_file_download_link_pac_code = uuid.UUID(data["test_file_download_link_pac_code"])
            self.test_conditional_file_download_link_pac_code = uuid.UUID(data["test_conditional_file_download_link_pac_code"])
            self.test_async_flow_req_link_pac_code = uuid.UUID(data["test_async_flow_req_link_pac_code"])
            self.test_conditional_async_flow_req_link_pac_code = uuid.UUID(data["test_conditional_async_flow_req_link_pac_code"])
            self.conditional_btn_example_link_plant_code = uuid.UUID(data["conditional_btn_example_link_plant_code"])

