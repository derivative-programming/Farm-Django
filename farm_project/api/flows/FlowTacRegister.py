from dataclasses import dataclass
from dataclasses_json import dataclass_json,LetterCase 
import uuid
from api.flows.base.BaseFlowTacRegister import BaseFlowTacRegister
from api.models import Tac 
from api.flows.base.LogSeverity import LogSeverity
from api.helpers import SessionContext
from api.models import Customer
from django.utils import timezone
from api.flows import ApiToken

@dataclass_json
@dataclass
class FlowTacRegisterResult():
    context_tac_code:uuid = uuid.UUID(int=0)
    customer_code:uuid = uuid.UUID(int=0)
    email:str = ""
    user_code_value:uuid = uuid.UUID(int=0)
    utc_offset_in_minutes:int = 0
    role_name_csv_list:str = ""
    api_key:str = ""

    def __init__(self): 
        pass

class FlowTacRegister(BaseFlowTacRegister):
    def __init__(self, session_context:SessionContext): 
        super(FlowTacRegister, self).__init__(session_context) 
    
    def process(self,
        tac: Tac,
        email:str,
        password:str,
        confirm_password:str,
        first_name:str,
        last_name:str
        ) -> FlowTacRegisterResult:

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Start")
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Code::" + str(tac.code))

        super()._process_validation_rules(
            tac,
            email,
            password,
            confirm_password,
            first_name,
            last_name,
        )

        super()._throw_queued_validation_errors()

        customer_code_output = uuid.UUID(int=0)
        email_output = ""
        user_code_value_output = uuid.UUID(int=0)
        utc_offset_in_minutes_output = 0
        role_name_csv_list_output = ""
        api_key_output = ""

        # TODO: add flow logic

        customer = Customer.objects.create()
        customer.tac = tac
        customer.email = email
        customer.password = password
        customer.code = uuid.uuid4() 
        customer.first_name = first_name
        customer.last_name = last_name
        # customer.registration_utc_date_time = timezone.now
        customer.is_active = True
        # customer.last_login_utc_date_time = timezone.now
        customer.last_change_code = uuid.uuid4() 
        customer.save()
        
        customer_code_output = customer.code
        email_output = customer.email
        user_code_value_output = customer.code
        utc_offset_in_minutes_output = customer.utc_offset_in_minutes
 
        role_name_csv_list_output = "" 

        api_key_dict = dict()
        api_key_dict["pac_code"] = str(customer.tac.pac.code)
        api_key_dict["tac_code"] = str(customer.tac.code)
        api_key_dict["customer_code"] = str(customer.code)
        api_key_dict["role_name_csv"] = role_name_csv_list_output
        api_key_output = ApiToken.create_token(api_key_dict, 1)
 


        super()._log_message_and_severity(LogSeverity.information_high_detail, "Building result")
        result = FlowTacRegisterResult() 
        result.context_tac_code = tac.code
        result.customer_code = customer_code_output
        result.email = email_output
        result.user_code_value = user_code_value_output
        result.utc_offset_in_minutes = utc_offset_in_minutes_output
        result.role_name_csv_list = role_name_csv_list_output
        result.api_key = api_key_output
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Result:" + result.to_json())

        super()._log_message_and_severity(LogSeverity.information_high_detail, "End")


        return result


    