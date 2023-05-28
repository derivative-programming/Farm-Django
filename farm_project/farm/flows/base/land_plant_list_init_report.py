import uuid
from farm.models import Land 
from .base_flow import BaseFlow
from farm.flows.base import LogSeverity
from farm.helpers import SessionContext
from decimal import Decimal
from datetime import date, datetime
from farm.helpers import TypeConversion
import farm.flows.constants.land_plant_list_init_report as FlowConstants
class BaseFlowLandPlantListInitReport(BaseFlow):
    def __init__(self, session_context:SessionContext): 
        super(BaseFlowLandPlantListInitReport, self).__init__(
            "LandPlantListInitReport", 
            session_context,
            ) 
    def _process_validation_rules(self, 
            land: Land,

        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")

        self._process_security_rules(land)
    def _process_security_rules(self, 
        land: Land,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")
