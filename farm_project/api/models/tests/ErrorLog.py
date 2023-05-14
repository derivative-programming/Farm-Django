from django.test import TestCase
from api.models.factories import ErrorLogFactory
from api.models import ErrorLog

class ErrorLogTestCase(TestCase):
    def setUp(self):
        self.error_log = ErrorLogFactory()

    def test_error_log_creation(self):
        self.assertIsInstance(self.error_log, ErrorLog)
        self.assertEqual(ErrorLog.objects.count(), 1)

    def test_error_log_fields(self): 
        self.assertIsInstance(self.error_log, ErrorLog)
        self.assertIsNotNone(self.error_log.error_log_id)
        self.assertIsNotNone(self.error_log.code)
        self.assertIsNotNone(self.error_log.insert_utc_date_time)
        self.assertIsNotNone(self.error_log.last_update_utc_date_time)
        self.assertIsNotNone(self.error_log.insert_user_id)
        self.assertIsNotNone(self.error_log.last_update_user_id)
        self.assertIsNotNone(self.error_log.last_change_code)
        self.assertIsNotNone(self.error_log.browser_code)
        self.assertIsNotNone(self.error_log.context_code)
        self.assertIsNotNone(self.error_log.created_utc_date_time)
        self.assertIsNotNone(self.error_log.description)
        self.assertIsNotNone(self.error_log.is_client_side_error)
        self.assertIsNotNone(self.error_log.is_resolved)
        self.assertIsNotNone(self.error_log.pac)
        self.assertIsNotNone(self.error_log.url)