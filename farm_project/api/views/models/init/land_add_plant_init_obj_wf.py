from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
import uuid
from dataclasses_json import dataclass_json, LetterCase, config   
from .get_init_response import GetInitResponse
from api.helpers import TypeConversion 
from api.flows import FlowLandAddPlantInitObjWFResult 

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandAddPlantGetInitResponse(GetInitResponse):
    landName:str=""
    tacCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
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
#endset

    def load_flow_response(self,data:FlowLandAddPlantInitObjWFResult): 
        self.landName = data.land_name
        self.tacCode = data.tac_code
        self.requestFlavorCode = data.request_flavor_code
        self.requestOtherFlavor = data.request_other_flavor
        self.requestSomeIntVal = data.request_some_int_val
        self.requestSomeBigIntVal = data.request_some_big_int_val
        self.requestSomeBitVal = data.request_some_bit_val
        self.requestIsEditAllowed = data.request_is_delete_allowed
        self.requestIsDeleteAllowed = data.request_is_edit_allowed
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
 
  