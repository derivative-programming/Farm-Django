import uuid
from api.models import Land 
from .base_flow import BaseFlow
from api.flows.base import LogSeverity
from api.helpers import SessionContext
from decimal import Decimal
from datetime import date, datetime
from api.helpers import TypeConversion
import api.flows.constants.land_add_plant as LandAddPlantConstants

class BaseFlowLandAddPlant(BaseFlow):
    def __init__(self, session_context:SessionContext): 
        super(BaseFlowLandAddPlant, self).__init__(
            "LandAddPlant", 
            session_context,
            ) 
     
    
    def _process_validation_rules(self, 
        land: Land,
        request_flavor_code:uuid = "",    
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
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")
  
        if request_flavor_code == "" and LandAddPlantConstants.param_request_flavor_code_isRequired == True:
            self._add_field_validation_error("requestFlavorCode","Please select a Flavor")
            
        if request_other_flavor == "" and LandAddPlantConstants.param_request_other_flavor_isRequired == True:
            self._add_field_validation_error("requestOtherFlavor","Please enter a Other Flavor")
            
        if request_some_int_val == 0 and LandAddPlantConstants.param_request_some_int_val_isRequired == True:
            self._add_field_validation_error("requestSomeIntVal","Please enter a Some Int Val")
            
        if request_some_big_int_val == 0 and LandAddPlantConstants.param_request_some_big_int_val_isRequired == True:
            self._add_field_validation_error("requestSomeBigIntVal","Please enter a Some Big Int Val")
            
        if request_some_bit_val == None and LandAddPlantConstants.param_request_some_bit_val_isRequired == True:
            self._add_field_validation_error("requestSomeBitVal","Please enter a Some Bit Val")
            
        if request_is_edit_allowed == None and LandAddPlantConstants.param_request_is_edit_allowed_isRequired == True:
            self._add_field_validation_error("requestIsEditAllowed","Please enter a Is Edit Allowed")
            
        if request_is_delete_allowed == None and LandAddPlantConstants.param_request_is_delete_allowed_isRequired == True:
            self._add_field_validation_error("requestIsDeleteAllowed","Please enter a Is Delete Allowed")
            
        if request_some_float_val == 0 and LandAddPlantConstants.param_request_some_float_val_isRequired == True:
            self._add_field_validation_error("requestSomeFloatVal","Please enter a Some Float Val")
            
        if request_some_decimal_val == 0 and LandAddPlantConstants.param_request_some_decimal_val_isRequired == True:
            self._add_field_validation_error("requestSomeDecimalVal","Please enter a Some Decimal Val")
            
        if request_some_utc_date_time_val == "" and LandAddPlantConstants.param_request_some_utc_date_time_val_isRequired == True:
            self._add_field_validation_error("requestSomeUTCDateTimeVal","Please enter a Some UTC Date Time Val")
            
        if request_some_date_val == "" and LandAddPlantConstants.param_request_some_date_val_isRequired == True:
            self._add_field_validation_error("requestSomeDateVal","Please enter a Some Date Val")
            
        if request_some_money_val == "" and LandAddPlantConstants.param_request_some_money_val_isRequired == True:
            self._add_field_validation_error("requestSomeMoneyVal","Please enter a Some Money Val")
            
        if request_some_n_var_char_val == "" and LandAddPlantConstants.param_request_some_n_var_char_val_isRequired == True:
            self._add_field_validation_error("requestSomeNVarCharVal","Please enter a Some N Var Char Val")
            
        if request_some_var_char_val == "" and LandAddPlantConstants.param_request_some_var_char_val_isRequired == True:
            self._add_field_validation_error("requestSomeVarCharVal","Please enter a Some Var Char Val")
            
        if request_some_text_val == "" and LandAddPlantConstants.param_request_some_text_val_isRequired == True:
            self._add_field_validation_error("requestSomeTextVal","Please enter a Some Text Val")
            
        if request_some_phone_number == "" and LandAddPlantConstants.param_request_some_phone_number_isRequired == True:
            self._add_field_validation_error("requestSomePhoneNumber","Please enter a Some Phone Number")
            
        if request_some_email_address == "" and LandAddPlantConstants.param_request_some_email_address_isRequired == True:
            self._add_field_validation_error("requestSomeEmailAddress","Please enter a Some Email Address")
            
        if request_sample_image_upload_file == "" and LandAddPlantConstants.param_request_sample_image_upload_file_isRequired == True:
            self._add_field_validation_error("requestSampleImageUploadFile","Please enter a Some Image Upload File")



        self._process_security_rules(land)
        
        
        

    
    def _process_security_rules(self, 
        land: Land,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")
