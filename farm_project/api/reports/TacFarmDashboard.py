from dataclasses import dataclass
import json
import uuid
from typing import List
from api.reports.providers.TacFarmDashboard import ReportProviderTacFarmDashboard
from api.reports.row_models import ReportItemTacFarmDashboard
import logging
from .ReportRequestValidationError import ReportRequestValidationError
 

class ReportTacFarmDashboard():
    def __init__(self): 
        pass
     
    def generate(self, 
                 tac_code:uuid,
                 page_number:int,
                 item_count_per_page:int,
                 order_by_column_name:str,
                 order_by_descending:bool,
                 ) -> List[ReportItemTacFarmDashboard]:
        logging.debug('ReportTacFarmDashboard.generate Start')

        if item_count_per_page <= 0:
            raise ReportRequestValidationError("item_count_per_page","Minimum count per page is 1")
        
        if page_number <= 0:
            raise ReportRequestValidationError("page_number","Minimum page number is 1")
        
        provider = ReportProviderTacFarmDashboard()

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
            reportItem.field_one_land_plant_list_link_plant_code = uuid.UUID(dataItem["field_one_land_plant_list_link_plant_code"])
            result.append(reportItem) 
            
        logging.debug("ReportTacFarmDashboard.generate Results: " + json.dumps(dataList))

        logging.debug('ReportTacFarmDashboard.generate End')
        return result
     

