import uuid
from api.models import Tac 
from api.flows.base.BaseFlow import BaseFlow
from api.flows.base.LogSeverity import LogSeverity
from api.helpers import SessionContext
 

class BaseFlowTacFarmDashboardInitReport(BaseFlow):
    def __init__(self, session_context:SessionContext): 
        super(BaseFlowTacFarmDashboardInitReport, self).__init__(
            "TacFarmDashboardInitReport", 
            session_context,
            ) 

    def _process_validation_rules(self, 
        tac: Tac,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")
        self._process_security_rules(tac)

    
    def _process_security_rules(self, 
        tac: Tac,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")


    