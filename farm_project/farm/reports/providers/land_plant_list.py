# reports/providers/land_plant_list.py
"""
This module contains the land plant list report provider used in the project.
"""
import json
import logging
from datetime import date, datetime
import uuid
from decimal import Decimal
from django.db import connection
from farm.reports.row_models import ReportItemLandPlantList
from farm.helpers import SessionContext

class ReportProviderLandPlantList():
    """
    The land plant list report provider.
    """
    _session_context:SessionContext
    def __init__(self, session_context:SessionContext):
        """
        This method initializes the land plant list report provider.
        """
        self._session_context = session_context

    def generate_list(self,
                    land_code: uuid.UUID,
                    some_int_val: int,
                    some_big_int_val: int,
                    some_bit_val: bool,
                    is_edit_allowed: bool,
                    is_delete_allowed: bool,
                    some_float_val: float,
                    some_decimal_val: Decimal,
                    some_min_utc_date_time_val: datetime,
                    some_min_date_val: date,
                    some_money_val: Decimal,
                    some_n_var_char_val: str,
                    some_var_char_val: str,
                    some_text_val: str,
                    some_phone_number: str,
                    some_email_address: str,
                    flavor_code: uuid.UUID,
                    page_number:int,
                    item_count_per_page:int,
                    order_by_column_name:str,
                    order_by_descending:bool,
                      ) -> list[dict[str,any]]:
        """
        This method generates the land plant list.
        """

        logging.debug("ReportProviderLandPlantList.generate_list Start")
        logging.debug("ReportProviderLandPlantList.generate_list land_code:" + str(land_code))

        offset = (page_number - 1) * item_count_per_page

        results = list()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    plant.code as plant_code,
                    plant.some_int_val as some_int_val,
                    plant.some_big_int_val as some_big_int_val,
                    plant.some_bit_val as some_bit_val,
                    plant.is_edit_allowed as is_edit_allowed,
                    plant.is_delete_allowed as is_delete_allowed,
                    plant.some_float_val as some_float_val,
                    plant.some_decimal_val as some_decimal_val,
                    plant.some_utc_date_time_val as some_utc_date_time_val,
                    plant.some_date_val as some_date_val,
                    plant.some_money_val as some_money_val,
                    plant.some_n_var_char_val as some_n_var_char_val,
                    plant.some_var_char_val as some_var_char_val,
                    plant.some_text_val as some_text_val,
                    plant.some_phone_number as some_phone_number,
                    plant.some_email_address as some_email_address,
                    flavor.name as flavor_name,
                    flavor.code as flavor_code,
                    plant.some_n_var_char_val as n_var_char_as_url,
                    plant.some_int_val as some_int_conditional_on_deletable,
                    plant.code as update_link_plant_code,
                    plant.code as delete_async_button_link_plant_code,
                    plant.code as details_link_plant_code,
                    pac.code as test_file_download_link_pac_code,
                    pac.code as test_conditional_file_download_link_pac_code,
                    pac.code as test_async_flow_req_link_pac_code,
                    pac.code as test_conditional_async_flow_req_link_pac_code,
                    plant.code as conditional_btn_example_link_plant_code
                from
                    farm_plant plant
                join farm_flavor flavor on plant.flvr_foreign_key_id = flavor.flavor_id
                join farm_land land on land.land_id = plant.land_id
                join farm_pac pac on land.pac_id = pac.pac_id
                WHERE land.code = %s
                """, (
                    str(land_code).replace('-', ''),
                    ))
            results = self.dictfetchall(cursor)

        logging.debug("ReportProviderLandPlantList.generate_list Results: " + json.dumps(results))

        logging.debug("ReportProviderLandPlantList.generate_list End")
        return results

    def dictfetchall(self, cursor) -> list[dict[str, any]]:
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
