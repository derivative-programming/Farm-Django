from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
import uuid
from dataclasses_json import dataclass_json, LetterCase, config   
from .get_init_response import GetInitResponse
from api.helpers import TypeConversion 
from api.flows import FlowLandPlantListInitReportResult 
from api.helpers import SessionContext 
from api.models import Land 
from api.flows import FlowLandPlantListInitReport
from api.flows import FlowValidationError
import api.views.models as view_models
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandPlantListInitReportGetInitModelResponse(GetInitResponse):
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
    flavorCode:uuid = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
    landCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
    tacCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
    landName:str=""
#endset
    def load_flow_response(self,data:FlowLandPlantListInitReportResult):
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
        self.flavorCode = data.flavor_code
        self.landCode = data.land_code
        self.tacCode = data.tac_code
        self.landName = data.land_name


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandPlantListInitReportGetInitModelRequest():
    
    def process_request(self,
                        session_context:SessionContext,
                        land:Land,
                        response:LandPlantListInitReportGetInitModelResponse) -> LandPlantListInitReportGetInitModelResponse:
        
        try:
            
            flow = FlowLandPlantListInitReport(session_context)
            flowResponse = flow.process(
                land
            ) 

            flowResponse = flow.process(
                land, 
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