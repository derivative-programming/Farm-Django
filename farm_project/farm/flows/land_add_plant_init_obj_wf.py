from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, config
from datetime import date, datetime
import uuid
from farm.flows.base import BaseFlowLandAddPlantInitObjWF
from farm.models import Land
from farm.flows.base import LogSeverity
from farm.helpers import SessionContext
from farm.models import Customer
from datetime import datetime, timezone
from farm.helpers import ApiToken
from decimal import Decimal
from farm.helpers import TypeConversion
import farm.models as farm_models
import farm.models.managers as farm_managers

@dataclass_json
@dataclass
class FlowLandAddPlantInitObjWFResult():
    request_flavor_code:str = ""
    request_other_flavor:str = ""
    request_some_int_val:int = 0
    request_some_big_int_val:int = 0
    request_some_bit_val:bool = False
    request_is_delete_allowed:bool = False
    request_is_edit_allowed:bool = False
    request_some_float_val:float = 0
    request_some_decimal_val:Decimal = Decimal(0)
    request_some_utc_date_time_val:datetime = field(default_factory=TypeConversion.get_default_date_time,
            metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat
        ))
    request_some_date_val:date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat,
            decoder=date.fromisoformat
        ))
    request_some_money_val:Decimal = Decimal(0)
    request_some_n_var_char_val:str = ""
    request_some_var_char_val:str = ""
    request_some_text_val:str = ""
    request_some_phone_number:str = ""
    request_some_email_address:str = ""
    tac_code: uuid.UUID = uuid.UUID(int=0)
    land_name:str = ""
    def __init__(self):
        pass
class FlowLandAddPlantInitObjWF(BaseFlowLandAddPlantInitObjWF):
    def __init__(self, session_context:SessionContext):
        super(FlowLandAddPlantInitObjWF, self).__init__(session_context)
    def process(self,
        land: Land,

        ) -> FlowLandAddPlantInitObjWFResult:
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Start")
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Code::" + str(land.code))
        super()._process_validation_rules(
            land,

        )
        super()._throw_queued_validation_errors()
        request_flavor_code_output:str = ""
        request_other_flavor_output:str = ""
        request_some_int_val_output:int = 0
        request_some_big_int_val_output:int = 0
        request_some_bit_val_output:bool = False
        request_is_delete_allowed_output:bool = False
        request_is_edit_allowed_output:bool = False
        request_some_float_val_output:float = 0
        request_some_decimal_val_output:Decimal = Decimal(0)
        request_some_utc_date_time_val_output:datetime = TypeConversion.get_default_date_time()
        request_some_date_val_output:date = TypeConversion.get_default_date()
        request_some_money_val_output:Decimal = 0
        request_some_n_var_char_val_output:str = ""
        request_some_var_char_val_output:str = ""
        request_some_text_val_output:str = ""
        request_some_phone_number_output:str = ""
        request_some_email_address_output:str = ""
        tac_code_output: uuid.UUID = uuid.UUID(int=0)
        land_name_output:str = ""
        # TODO: add flow logic

        plant:farm_models.Plant = farm_models.Plant.build(land)
        request_flavor_code_output = plant.flvr_foreign_key.code
        request_other_flavor_output = plant.other_flavor
        request_some_int_val_output = plant.some_int_val
        request_some_big_int_val_output = plant.some_big_int_val
        request_some_bit_val_output = plant.some_bit_val
        request_is_delete_allowed_output = plant.is_delete_allowed
        request_is_edit_allowed_output = plant.is_edit_allowed
        request_some_float_val_output = plant.some_float_val
        request_some_decimal_val_output = plant.some_decimal_val
        request_some_utc_date_time_val_output = plant.some_utc_date_time_val
        request_some_date_val_output = plant.some_date_val
        request_some_money_val_output = plant.some_money_val
        request_some_n_var_char_val_output = plant.some_n_var_char_val
        request_some_var_char_val_output = plant.some_var_char_val
        request_some_text_val_output = plant.some_text_val
        request_some_phone_number_output = plant.some_phone_number
        request_some_email_address_output = plant.some_email_address
        tac_code_output = farm_models.Tac.objects.from_enum(enum_val=farm_managers.TacEnum.Primary).code
        land_name_output = land.name

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Building result")
        result = FlowLandAddPlantInitObjWFResult()
        result.request_flavor_code = request_flavor_code_output
        result.request_other_flavor = request_other_flavor_output
        result.request_some_int_val = request_some_int_val_output
        result.request_some_big_int_val = request_some_big_int_val_output
        result.request_some_bit_val = request_some_bit_val_output
        result.request_is_delete_allowed = request_is_delete_allowed_output
        result.request_is_edit_allowed = request_is_edit_allowed_output
        result.request_some_float_val = request_some_float_val_output
        result.request_some_decimal_val = request_some_decimal_val_output
        result.request_some_utc_date_time_val = request_some_utc_date_time_val_output
        result.request_some_date_val = request_some_date_val_output
        result.request_some_money_val = request_some_money_val_output
        result.request_some_n_var_char_val = request_some_n_var_char_val_output
        result.request_some_var_char_val = request_some_var_char_val_output
        result.request_some_text_val = request_some_text_val_output
        result.request_some_phone_number = request_some_phone_number_output
        result.request_some_email_address = request_some_email_address_output
        result.tac_code = tac_code_output
        result.land_name = land_name_output
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Result:" + result.to_json())
        super()._log_message_and_severity(LogSeverity.information_high_detail, "End")
        return result
