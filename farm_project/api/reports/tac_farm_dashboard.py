from dataclasses import dataclass
import json
import uuid
from typing import List
from api.reports.providers import ReportProviderTacFarmDashboard
from api.reports.row_models import ReportItemTacFarmDashboard
import logging
from .report_request_validation_error import ReportRequestValidationError
from api.helpers import SessionContext
 

class ReportManagerTacFarmDashboard():
    _session_context:SessionContext
    def __init__(self, session_context:SessionContext): 
        self._session_context = session_context
     
    def generate(self, 
                 tac_code:uuid,
                 page_number:int,
                 item_count_per_page:int,
                 order_by_column_name:str,
                 order_by_descending:bool,
                 ) -> List[ReportItemTacFarmDashboard]:
        logging.debug('ReportManagerTacFarmDashboard.generate Start')

        if item_count_per_page <= 0:
            raise ReportRequestValidationError("item_count_per_page","Minimum count per page is 1")
        
        if page_number <= 0:
            raise ReportRequestValidationError("page_number","Minimum page number is 1")
        
        provider = ReportProviderTacFarmDashboard(self._session_context)

        dataList = provider.generate_list(
            tac_code,
            page_number,
            item_count_per_page,
            order_by_column_name,
            order_by_descending,
            )

        result = list()

        for dataItem in dataList:
            reportItem = ReportItemTacFarmDashboard()
            reportItem.load_data_provider_dict(dataItem)
            result.append(reportItem) 
            
        logging.debug("ReportManagerTacFarmDashboard.generate Results: " + json.dumps(dataList))

        logging.debug('ReportManagerTacFarmDashboard.generate End')
        return result
     

