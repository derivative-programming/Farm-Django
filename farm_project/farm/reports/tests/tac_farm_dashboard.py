from unittest import TestCase
from unittest.mock import patch, MagicMock
from farm.reports import ReportManagerTacFarmDashboard, ReportRequestValidationError
from farm.reports.row_models import ReportItemTacFarmDashboard
import uuid
from farm.helpers import SessionContext
from farm.models import CurrentRuntime

class ReportTestTacFarmDashboard(TestCase):

    def setUp(self):
        CurrentRuntime.initialize()
        session_context = SessionContext(dict())
        self.tac_code = uuid.uuid4()
        self.page_number = 1
        self.item_count_per_page = 10
        self.order_by_column_name = "code"
        self.order_by_descending = False
        self.report = ReportManagerTacFarmDashboard(session_context)

    # @patch('farm.reports.providers.tac_farm_dashboard.ReportProviderTacFarmDashboard')
    # def test_generate(self, MockProvider):
    #     mock_provider = MockProvider.return_value
    #     mock_provider.generate_list.return_value = [
    #         {"field_one_plant_list_link_land_code": str(self.tac_code)},
    #         {"conditional_btn_example_link_land_code": str(self.tac_code)},
    #         {"is_conditional_btn_available": False}
    #     ]

    #     result = self.report.generate(
    #         self.tac_code,
    #         self.page_number,
    #         self.item_count_per_page,
    #         self.order_by_column_name,
    #         self.order_by_descending
    #     )

    #     self.assertIsInstance(result, list)
    #     for item in result:
    #         self.assertIsInstance(item, ReportItemTacFarmDashboard)
    #         self.assertEqual(item.field_one_plant_list_link_land_code, self.tac_code)
    #         self.assertEqual(item.conditional_btn_example_link_land_code, self.tac_code)
    #         self.assertEqual(item.is_conditional_btn_available, True)

    def test_generate_invalid_item_count_per_page(self):
        with self.assertRaises(ReportRequestValidationError):
            self.report.generate(
                self.tac_code,
                self.page_number,
                0,
                self.order_by_column_name,
                self.order_by_descending
            )

    def test_generate_invalid_page_number(self):
        with self.assertRaises(ReportRequestValidationError):
            self.report.generate(
                self.tac_code,
                0,
                self.item_count_per_page,
                self.order_by_column_name,
                self.order_by_descending
            )
