
from dataclasses import dataclass
from dataclasses_json import dataclass_json,LetterCase 
import uuid
import api.flows.base
from api.flows.base.BaseFlowTacFarmDashboardInitReport import BaseFlowTacFarmDashboardInitReport 
from api.models import Tac 
from api.flows.base.LogSeverity import LogSeverity

@dataclass_json
@dataclass
class FlowTacFarmDashboardInitReportResult():
    context_tac_code:uuid = uuid.UUID(int=0)
    customer_code:uuid = uuid.UUID(int=0)

    def __init__(self): 
        pass

class FlowTacFarmDashboardInitReport(BaseFlowTacFarmDashboardInitReport):
    def __init__(self): 
        super(FlowTacFarmDashboardInitReport, self).__init__() 

    def process(self, 
        tac: Tac,
        ) -> FlowTacFarmDashboardInitReportResult:
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Start")
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Code::" + str(tac.code))

        super()._process_validation_rules(
            tac,
        )

        super()._throw_queued_validation_errors()
        
        customer_code_output = uuid.UUID(int=0)
    
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Building result")
        result = FlowTacFarmDashboardInitReportResult()
        result.customer_code = customer_code_output
        result.context_tac_code = tac.code
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Result:" + result.to_json())
        
        super()._log_message_and_severity(LogSeverity.information_high_detail, "End")
        return result


    