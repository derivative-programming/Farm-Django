# flows/base/tests/base_flow.py
"""
test cases for base flow
"""
from django.test import TestCase
from unittest.mock import patch
from farm.flows.base import BaseFlow
from farm.flows.base import FlowValidationError
from farm.helpers import SessionContext

class TestBaseFlow(TestCase):
    """
    Test cases for base flow
    """
    def setUp(self):
        """
        setup for test cases
        """
        session_context = SessionContext(dict())
        self.base_flow = BaseFlow("TestFlow",session_context=session_context)

    def test_init(self):
        """
        test case for init
        """
        self.assertEqual(self.base_flow._BaseFlow__flow_name, "TestFlow")

    def test_add_validation_error(self):
        """
        test case for add_validation_error
        """
        self.base_flow._add_validation_error("Test error message")
        self.assertEqual(self.base_flow.queued_validation_errors, {"": "Test error message"})

    def test_add_field_validation_error(self):
        """
        test case for add_field_validation_error
        """
        self.base_flow._add_field_validation_error("field1", "Test error message")
        self.assertEqual(self.base_flow.queued_validation_errors, {"field1": "Test error message"})

    def test_add_field_validation_error_existing_field(self):
        """
        test case for add_field_validation_error with existing field
        """
        self.base_flow.queued_validation_errors = {"field1": "Existing error message"}
        self.base_flow._add_field_validation_error("field1", "Test error message")
        self.assertEqual(self.base_flow.queued_validation_errors, {"field1": "Existing error message,Test error message"})

    def test_throw_validation_error(self):
        """
        test case for throw_validation_error
        """
        with self.assertRaises(FlowValidationError) as context:
            self.base_flow._throw_validation_error("Test error message")
        self.assertEqual(context.exception.error_dict, {"": "Test error message"})

    def test_throw_field_validation_error(self):
        """
        test case for throw_field_validation_error
        """
        with self.assertRaises(FlowValidationError) as context:
            self.base_flow._throw_field_validation_error("field1", "Test error message")
        self.assertEqual(context.exception.error_dict, {"field1": "Test error message"})

    def test_throw_queued_validation_errors(self):
        """
        test case for throw_queued_validation_errors
        """
        self.base_flow.queued_validation_errors = {"field1": "Test error message"}
        with self.assertRaises(FlowValidationError) as context:
            self.base_flow._throw_queued_validation_errors()
        self.assertEqual(context.exception.error_dict, {"field1": "Test error message"})

    @patch("logging.error")
    def test_log_exception(self, logging_error_mock):
        """
        test case for log_exception
        """
        exception = Exception("Test exception")
        self.base_flow._log_exception(exception)
        logging_error_mock.assert_called_once_with("TestFlow Test exception")

    @patch("logging.debug")
    def test_log_message(self, logging_debug_mock):
        """
        test case for log_message
        """
        self.base_flow._log_message("Test message")
        logging_debug_mock.assert_called_once_with("TestFlow Test message")
