import json
import uuid
from django.db import connection
from api.reports.row_models import ReportItemTacFarmDashboard
import logging
from api.helpers import SessionContext

class ReportProviderTacFarmDashboard(): 
    _session_context:SessionContext
    def __init__(self, session_context:SessionContext): 
        self._session_context = session_context
    
    def generate_list(self, 
                    tacCode:uuid,
                    page_number:int,
                    item_count_per_page:int,
                    order_by_column_name:str,
                    order_by_descending:bool,
                      ) -> list[dict[str,any]]: 
        
        logging.debug("ReportProviderTacFarmDashboard.generate_list Start")
        logging.debug("ReportProviderTacFarmDashboard.generate_list tacCode:" + str(tacCode))
        
        offset = (page_number - 1) * item_count_per_page
        
        results = list()

        with connection.cursor() as cursor: 
            
            cursor.execute(""" 
                SELECT 
                    tac.code as field_one_land_plant_list_link_plant_code
                from api_tac tac
                WHERE tac.code = %s
                """, (
                    str(tacCode).replace('-', ''),  
                    ))
            results = self.dictfetchall(cursor)
             
        logging.debug("ReportProviderTacFarmDashboard.generate_list Results: " + json.dumps(results))

        logging.debug("ReportProviderTacFarmDashboard.generate_list End")
        return results

    def dictfetchall(self, cursor) -> list[dict[str,any]]:
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]