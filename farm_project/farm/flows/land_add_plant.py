from dataclasses import dataclass, field
from dataclasses_json import dataclass_json,LetterCase, config
from datetime import date, datetime
import uuid
from farm.flows.base import BaseFlowLandAddPlant
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
class FlowLandAddPlantResult():
    context_object_code: uuid.UUID = uuid.UUID(int=0)
    land_code: uuid.UUID = uuid.UUID(int=0)
    plant_code: uuid.UUID = uuid.UUID(int=0)
    output_flavor_code: uuid.UUID = uuid.UUID(int=0)
    output_other_flavor:str = ""
    output_some_int_val:int = 0
    output_some_big_int_val:int = 0
    output_some_bit_val:bool = False
    output_is_edit_allowed:bool = False
    output_is_delete_allowed:bool = False
    output_some_float_val:float = 0
    output_some_decimal_val:Decimal = Decimal(0)
    output_some_utc_date_time_val:datetime = field(default_factory=TypeConversion.get_default_date_time,
            metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat
        ))
    output_some_date_val:date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat,
            decoder=date.fromisoformat
        ))
    output_some_money_val:Decimal = Decimal(0)
    output_some_n_var_char_val:str = ""
    output_some_var_char_val:str = ""
    output_some_text_val:str = ""
    output_some_phone_number:str = ""
    output_some_email_address:str = ""

    def __init__(self):
        pass

class FlowLandAddPlant(BaseFlowLandAddPlant):
    def __init__(self, session_context:SessionContext):
        super(FlowLandAddPlant, self).__init__(session_context)

    def process(self,
        land: Land,
        request_flavor_code: uuid.UUID = uuid.UUID(int=0),
        request_other_flavor:str = "",
        request_some_int_val:int = 0,
        request_some_big_int_val:int = 0,
        request_some_bit_val:bool = False,
        request_is_edit_allowed:bool = False,
        request_is_delete_allowed:bool = False,
        request_some_float_val:float = 0,
        request_some_decimal_val:Decimal = 0,
        request_some_utc_date_time_val:datetime = TypeConversion.get_default_date_time(),
        request_some_date_val:date = TypeConversion.get_default_date(),
        request_some_money_val:Decimal = 0,
        request_some_n_var_char_val:str = "",
        request_some_var_char_val:str = "",
        request_some_text_val:str = "",
        request_some_phone_number:str = "",
        request_some_email_address:str = "",
        request_sample_image_upload_file:str = "",
        ) -> FlowLandAddPlantResult:

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Start")
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Code::" + str(land.code))

        super()._process_validation_rules(
            land,
            request_flavor_code,
            request_other_flavor,
            request_some_int_val,
            request_some_big_int_val,
            request_some_bit_val,
            request_is_edit_allowed,
            request_is_delete_allowed,
            request_some_float_val,
            request_some_decimal_val,
            request_some_utc_date_time_val,
            request_some_date_val,
            request_some_money_val,
            request_some_n_var_char_val,
            request_some_var_char_val,
            request_some_text_val,
            request_some_phone_number,
            request_some_email_address,
            request_sample_image_upload_file,
        )

        super()._throw_queued_validation_errors()

        land_code_output: uuid.UUID = uuid.UUID(int=0)
        plant_code_output: uuid.UUID = uuid.UUID(int=0)
        output_flavor_code_output:str = ""
        output_other_flavor_output:str = ""
        output_some_int_val_output:int = 0
        output_some_big_int_val_output:int = 0
        output_some_bit_val_output:bool = False
        output_is_edit_allowed_output:bool = False
        output_is_delete_allowed_output:bool = False
        output_some_float_val_output:float = 0
        output_some_decimal_val_output:Decimal = Decimal(0)
        output_some_utc_date_time_val_output:datetime = TypeConversion.get_default_date_time()
        output_some_date_val_output:date = TypeConversion.get_default_date()
        output_some_money_val_output:Decimal = 0
        output_some_n_var_char_val_output:str = ""
        output_some_var_char_val_output:str = ""
        output_some_text_val_output:str = ""
        output_some_phone_number_output:str = ""
        output_some_email_address_output:str = ""

        # TODO: add flow logic
##GENTrainingBlock[caseFlowLogic]Start
##GENLearn[calculatedIsTrueParentChild=true,calculatedIsTargetChildObjectAvailable=true,calculatedIsInitObjWF=false,isLoginPage=false]Start

        # plant:farm_models.Plant = farm_models.Plant.build(land)
        # plant.land = land
        # plant.flvr_foreign_key = farm_models.Flavor.objects.from_code(request_flavor_code)
        # plant.other_flavor = request_other_flavor
        # plant.some_int_val = request_some_int_val
        # plant.some_big_int_val = request_some_big_int_val
        # plant.some_bit_val = request_some_bit_val
        # plant.is_edit_allowed = request_is_edit_allowed
        # plant.is_delete_allowed = request_is_delete_allowed
        # plant.some_float_val = request_some_float_val
        # plant.some_decimal_val = request_some_decimal_val
        # plant.some_utc_date_time_val = request_some_utc_date_time_val
        # plant.some_date_val = request_some_date_val
        # plant.some_money_val = request_some_money_val
        # plant.some_n_var_char_val = request_some_n_var_char_val
        # plant.some_var_char_val = request_some_var_char_val
        # plant.some_text_val = request_some_text_val
        # plant.some_phone_number = request_some_phone_number
        # plant.some_email_address = request_some_email_address
        # plant.some_int_val = request_sample_image_upload_file
        # plant.save()

        # land_code_output: uuid.UUID = land.code
        # plant_code_output: uuid.UUID = plant.code
        # output_flavor_code_output = plant.flvr_foreign_key.code
        # output_other_flavor_output = plant.other_flavor
        # output_some_int_val_output = plant.some_int_val
        # output_some_big_int_val_output = plant.some_big_int_val
        # output_some_bit_val_output = plant.some_bit_val
        # output_is_edit_allowed_output = plant.is_edit_allowed
        # output_is_delete_allowed_output = plant.is_delete_allowed
        # output_some_float_val_output = plant.some_float_val
        # output_some_decimal_val_output = plant.some_decimal_val
        # output_some_utc_date_time_val_output = plant.some_utc_date_time_val
        # output_some_date_val_output = plant.some_date_val
        # output_some_money_val_output = plant.some_money_val
        # output_some_n_var_char_val_output = plant.some_n_var_char_val
        # output_some_var_char_val_output = plant.some_var_char_val
        # output_some_text_val_output = plant.some_text_val
        # output_some_phone_number_output = plant.some_phone_number
        # output_some_email_address_output = plant.some_email_address

##GENLearn[calculatedIsTrueParentChild=true,calculatedIsTargetChildObjectAvailable=true,calculatedIsInitObjWF=false,isLoginPage=false]End
##GENTrainingBlock[caseFlowLogic]End

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Building result")
        result = FlowLandAddPlantResult()

        result.context_object_code = land.code
        result.land_code = land_code_output
        result.plant_code = plant_code_output
        result.output_flavor_code = output_flavor_code_output
        result.output_other_flavor = output_other_flavor_output
        result.output_some_int_val = output_some_int_val_output
        result.output_some_big_int_val = output_some_big_int_val_output
        result.output_some_bit_val = output_some_bit_val_output
        result.output_is_edit_allowed = output_is_edit_allowed_output
        result.output_is_delete_allowed = output_is_delete_allowed_output
        result.output_some_float_val = output_some_float_val_output
        result.output_some_decimal_val = output_some_decimal_val_output
        result.output_some_utc_date_time_val = output_some_utc_date_time_val_output
        result.output_some_date_val = output_some_date_val_output
        result.output_some_money_val = output_some_money_val_output
        result.output_some_n_var_char_val = output_some_n_var_char_val_output
        result.output_some_var_char_val = output_some_var_char_val_output
        result.output_some_text_val = output_some_text_val_output
        result.output_some_phone_number = output_some_phone_number_output
        result.output_some_email_address = output_some_email_address_output

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Result:" + result.to_json())

        super()._log_message_and_severity(LogSeverity.information_high_detail, "End")


        return result


