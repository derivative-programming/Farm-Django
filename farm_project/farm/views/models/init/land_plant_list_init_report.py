from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from farm.views.models import ValidationError
from typing import List
import uuid
from dataclasses_json import dataclass_json, LetterCase, config
from farm.helpers import TypeConversion
from farm.flows import FlowLandPlantListInitReportResult
from farm.helpers import SessionContext
from farm.models import Land
from farm.flows import FlowLandPlantListInitReport
from farm.flows import FlowValidationError
import farm.views.models as view_models
import logging
from farm.models import Land
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandPlantListInitReportGetInitModelResponse():
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)
    someIntVal:int = 0
    someBigIntVal:int = 0
    someBitVal:bool = False
    isEditAllowed:bool = False
    isDeleteAllowed:bool = False
    someFloatVal:float = 0
    someDecimalVal:Decimal = Decimal(0)
    someMinUTCDateTimeVal:datetime = field(default_factory=TypeConversion.get_default_date_time,
            metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat
        ))
    someMinDateVal:datetime.date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat,
            decoder=date.fromisoformat
        ))
    someMoneyVal:Decimal = Decimal(0)
    someNVarCharVal:str = ""
    someVarCharVal:str = ""
    someTextVal:str = ""
    somePhoneNumber:str = ""
    someEmailAddress:str = ""
    landCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
    tacCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
    landName:str=""
#endset
    def load_flow_response(self,data:FlowLandPlantListInitReportResult):
        self.validation_errors = list()
        self.success = False
        self.message = ""
        self.someIntVal = data.some_int_val
        self.someBigIntVal = data.some_big_int_val
        self.someBitVal = data.some_bit_val
        self.isEditAllowed = data.is_edit_allowed
        self.isDeleteAllowed = data.is_delete_allowed
        self.someFloatVal = data.some_float_val
        self.someDecimalVal = data.some_decimal_val
        self.someMinUTCDateTimeVal = data.some_min_utc_date_time_val
        self.someMinDateVal = data.some_min_date_val
        self.someMoneyVal = data.some_money_val
        self.someNVarCharVal = data.some_n_var_char_val
        self.someVarCharVal = data.some_var_char_val
        self.someTextVal = data.some_text_val
        self.somePhoneNumber = data.some_phone_number
        self.someEmailAddress = data.some_email_address
        self.landCode = data.land_code
        self.tacCode = data.tac_code
        self.landName = data.land_name
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandPlantListInitReportGetInitModelRequest():
    def process_request(self,
                        session_context:SessionContext,
                        land_code: uuid.UUID,
                        response:LandPlantListInitReportGetInitModelResponse) -> LandPlantListInitReportGetInitModelResponse:
        try:
            logging.debug("loading model...")
            land = Land.objects.get(code=land_code)
            logging.debug("process request...")
            flow = FlowLandPlantListInitReport(session_context)
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

