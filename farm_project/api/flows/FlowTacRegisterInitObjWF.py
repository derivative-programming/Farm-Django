from dataclasses import dataclass
from dataclasses_json import dataclass_json,LetterCase 
import uuid
from api.flows.base.BaseFlowTacRegisterInitObjWF import BaseFlowTacRegisterInitObjWF
from api.models import Tac 
from api.flows.base.LogSeverity import LogSeverity

@dataclass_json
@dataclass
class FlowTacRegisterInitObjWFResult():
    context_tac_code:uuid = uuid.UUID(int=0)
    email:str = ""
    password:str = ""
    confirm_password:str = ""
    first_name:str = ""
    last_name:str = ""

    def __init__(self): 
        pass

class FlowTacRegisterInitObjWF(BaseFlowTacRegisterInitObjWF):
    def __init__(self): 
        super(FlowTacRegisterInitObjWF, self).__init__() 

    def process(self,
        tac: Tac,
        ) -> FlowTacRegisterInitObjWFResult:
 
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Start")
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Code::" + str(tac.code))

        super()._process_validation_rules(
            tac,
        )

        super()._throw_queued_validation_errors()

        email_output = ""
        password_output = ""
        confirm_password_output = ""
        first_name_output = ""
        last_name_output = ""
        

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Building result")
        result = FlowTacRegisterInitObjWFResult()
        result.email = email_output
        result.password = password_output
        result.confirm_password = confirm_password_output
        result.first_name = first_name_output
        result.last_name = last_name_output
        result.context_tac_code = tac.code
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Result:" + result.to_json())

        super()._log_message_and_severity(LogSeverity.information_high_detail, "End")


        return result


    