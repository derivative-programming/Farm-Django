import uuid
from api.models import Land 
from .base_flow import BaseFlow
from api.flows.base import LogSeverity
from api.helpers import SessionContext
from decimal import Decimal
from datetime import date, datetime
from api.helpers import TypeConversion

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
        self._process_security_rules(land)
        

    
    def _process_security_rules(self, 
        land: Land,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")
