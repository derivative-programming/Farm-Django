from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
import uuid
from dataclasses_json import dataclass_json, LetterCase, config
from farm.helpers import TypeConversion
from .post_reponse import PostResponse
from farm.flows import FlowLandAddPlantResult
from farm.flows import FlowLandAddPlant
from farm.helpers import SessionContext
from farm.models import Land
from farm.flows import FlowValidationError
import farm.views.models as view_models
import logging
from farm.models import Land
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandAddPlantPostModelResponse(PostResponse):
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
    land_code: uuid.UUID = uuid.UUID(int=0)
    plant_code: uuid.UUID = uuid.UUID(int=0)
#endset
    def load_flow_response(self,data:FlowLandAddPlantResult):
        placeholder = "" #to avoid pass line
        self.output_flavor_code = data.land_code
        self.output_other_flavor = data.output_other_flavor
        self.output_some_int_val = data.output_some_int_val
        self.output_some_big_int_val = data.output_some_big_int_val
        self.output_some_bit_val = data.output_some_bit_val
        self.output_is_edit_allowed = data.output_is_edit_allowed
        self.output_is_delete_allowed = data.output_is_delete_allowed
        self.output_some_float_val = data.output_some_float_val
        self.output_some_decimal_val = data.output_some_decimal_val
        self.output_some_utc_date_time_val = data.output_some_utc_date_time_val
        self.output_some_date_val = data.output_some_date_val
        self.output_some_money_val = data.output_some_money_val
        self.output_some_n_var_char_val = data.output_some_n_var_char_val
        self.output_some_var_char_val = data.output_some_var_char_val
        self.output_some_text_val = data.output_some_text_val
        self.output_some_phone_number = data.output_some_phone_number
        self.output_some_email_address = data.output_some_email_address
        self.land_code = data.land_code
        self.plant_code = data.plant_code
#endset
### request. expect camel case. use marshmallow to validate.
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandAddPlantPostModelRequest:
    requestFlavorCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
    requestOtherFlavor:str = ""
    requestSomeIntVal:int = 0
    requestSomeBigIntVal:int = 0
    requestSomeBitVal:bool = False
    requestIsEditAllowed:bool = False
    requestIsDeleteAllowed:bool = False
    requestSomeFloatVal:float = 0
    requestSomeDecimalVal:Decimal = Decimal(0)
    requestSomeUTCDateTimeVal:datetime = field(default_factory=TypeConversion.get_default_date_time,
            metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat
        ))
    requestSomeDateVal:date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat,
            decoder=date.fromisoformat
        ))
    requestSomeMoneyVal:Decimal = Decimal(0)
    requestSomeNVarCharVal:str = ""
    requestSomeVarCharVal:str = ""
    requestSomeTextVal:str = ""
    requestSomePhoneNumber:str = ""
    requestSomeEmailAddress:str = ""
    requestSampleImageUploadFile:str = ""
#endset
    def process_request(self,
                        session_context:SessionContext,
                        land_code: uuid.UUID,
                        response:LandAddPlantPostModelResponse) -> LandAddPlantPostModelResponse:
        try:
            logging.debug("loading model...")
            land = Land.objects.get(code=land_code)
            flow = FlowLandAddPlant(session_context)
            logging.debug("process flow...")
            flowResponse = flow.process(
                land,
                self.requestFlavorCode,
                self.requestOtherFlavor,
                self.requestSomeIntVal,
                self.requestSomeBigIntVal,
                self.requestSomeBitVal,
                self.requestIsEditAllowed,
                self.requestIsDeleteAllowed,
                self.requestSomeFloatVal,
                self.requestSomeDecimalVal,
                self.requestSomeUTCDateTimeVal,
                self.requestSomeDateVal,
                self.requestSomeMoneyVal,
                self.requestSomeNVarCharVal,
                self.requestSomeVarCharVal,
                self.requestSomeTextVal,
                self.requestSomePhoneNumber,
                self.requestSomeEmailAddress,
                self.requestSampleImageUploadFile,
#endset
            )
            response.load_flow_response(flowResponse);
            response.success = True
            response.message = "Success."
        except FlowValidationError as ve:
            response.success = False
            response.validation_errors = list()
            for key in ve.error_dict:
                response.validation_errors.append(view_models.ValidationError(key,ve.error_dict[key]))
        return response

