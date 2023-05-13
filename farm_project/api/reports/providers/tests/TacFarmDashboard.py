from django.test import TestCase
from api.reports.providers import ReportProviderTacFarmDashboard
import uuid
from api.helpers import SessionContext

class ReportProviderTacFarmDashboardTest(TestCase):

    def setUp(self):
        session_context = SessionContext(dict())
        self.report_provider = ReportProviderTacFarmDashboard(session_context)
        self.tacCode = uuid.uuid4()  # replace with a valid UUID from your test database
        self.page_number = 1
        self.item_count_per_page = 10
        self.order_by_column_name = "code"  # replace with a valid column name
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
            self.assertIn("field_one_land_plant_list_link_plant_code", result)
            self.assertEqual(result["field_one_land_plant_list_link_plant_code"], str(self.tacCode).replace('-', ''))