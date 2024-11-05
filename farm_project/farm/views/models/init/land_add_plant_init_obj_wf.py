from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from farm.views.models import ValidationError
from typing import List
import uuid
from dataclasses_json import dataclass_json, LetterCase, config
from farm.helpers import TypeConversion
from farm.flows import FlowLandAddPlantInitObjWFResult
from farm.helpers import SessionContext
from farm.models import Land
from farm.flows import FlowLandAddPlantInitObjWF
from farm.flows import FlowValidationError
import farm.views.models as view_models
import logging
from farm.models import Land
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandAddPlantInitObjWFGetInitModelResponse():
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)
    requestFlavorCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
    requestOtherFlavor:str = ""
    requestSomeIntVal:int = 0
    requestSomeBigIntVal:int = 0
    requestSomeBitVal:bool = False
    requestIsDeleteAllowed:bool = False
    requestIsEditAllowed:bool = False
    requestSomeFloatVal:float = 0
    requestSomeDecimalVal:Decimal = Decimal(0)
    requestSomeUTCDateTimeVal:datetime = field(default_factory=TypeConversion.get_default_date_time,
            metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat
        ))
    requestSomeDateVal:datetime.date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat,
            decoder=date.fromisoformat
        ))
    requestSomeMoneyVal:Decimal = Decimal(0)
    requestSomeNVarCharVal:str = ""
    requestSomeVarCharVal:str = ""
    requestSomeTextVal:str = ""
    requestSomePhoneNumber:str = ""
    requestSomeEmailAddress:str = ""
    landName:str=""
    tacCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
#endset
    def load_flow_response(self,data:FlowLandAddPlantInitObjWFResult):
        self.validation_errors = list()
        self.success = False
        self.message = ""
        self.requestFlavorCode = data.request_flavor_code
        self.requestOtherFlavor = data.request_other_flavor
        self.requestSomeIntVal = data.request_some_int_val
        self.requestSomeBigIntVal = data.request_some_big_int_val
        self.requestSomeBitVal = data.request_some_bit_val
        self.requestIsDeleteAllowed = data.request_is_delete_allowed
        self.requestIsEditAllowed = data.request_is_edit_allowed
        self.requestSomeFloatVal = data.request_some_float_val
        self.requestSomeDecimalVal = data.request_some_decimal_val
        self.requestSomeUTCDateTimeVal = data.request_some_utc_date_time_val
        self.requestSomeDateVal = data.request_some_date_val
        self.requestSomeMoneyVal = data.request_some_money_val
        self.requestSomeNVarCharVal = data.request_some_n_var_char_val
        self.requestSomeVarCharVal = data.request_some_var_char_val
        self.requestSomeTextVal = data.request_some_text_val
        self.requestSomePhoneNumber = data.request_some_phone_number
        self.requestSomeEmailAddress = data.request_some_email_address
        self.landName = data.land_name
        self.tacCode = data.tac_code
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandAddPlantInitObjWFGetInitModelRequest():
    def process_request(self,
                        session_context:SessionContext,
                        land_code: uuid.UUID,
                        response:LandAddPlantInitObjWFGetInitModelResponse) -> LandAddPlantInitObjWFGetInitModelResponse:
        try:
            logging.debug("loading model...")
            land = Land.objects.get(code=land_code)
            logging.debug("process request...")
            flow = FlowLandAddPlantInitObjWF(session_context)
            flowResponse = flow.process(
                land
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

