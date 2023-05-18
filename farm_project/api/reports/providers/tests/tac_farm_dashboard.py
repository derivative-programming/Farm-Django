from django.test import TestCase
from api.reports.providers import ReportProviderTacFarmDashboard
import uuid
from api.helpers import SessionContext
from api.models.factories import TacFactory

class ReportProviderTacFarmDashboardTest(TestCase):

    def setUp(self):
        session_context = SessionContext(dict())
        self.report_provider = ReportProviderTacFarmDashboard(session_context)
        self.tac = TacFactory.create()
        self.tacCode = self.tac.code 
        self.page_number = 1
        self.item_count_per_page = 10
        self.order_by_column_name = ""  
        self.order_by_descending = False

    def test_generate_list(self):
        results = self.report_provider.generate_list(
            self.tacCode, 
            self.page_number,
            self.item_count_per_page,
            self.order_by_column_name,
            self.order_by_descending
        )
        self.assertIsInstance(results, list)
        for result in results:
            self.assertIsInstance(result, dict)
            self.assertIn("field_one_plant_list_link_land_code", result)
            self.assertEqual(result["field_one_plant_list_link_land_code"], str(self.tacCode).replace('-', ''))