# flows/base/tests/flow_validation_error.py
"""
Tests for the FlowValidationError class.
"""
from django.test import TestCase
from farm.flows.base import FlowValidationError

class TestFlowValidationError(TestCase):
    """
    Tests for the FlowValidationError class.
    """
    def test_init_with_message(self):
        """
        Tests the initialization of the FlowValidationError class with a message.
        """
        exception = FlowValidationError(None, "Test error message", None)
        self.assertEqual(exception.error_dict, {"": "Test error message"})

    def test_init_with_field_name_and_message(self):
        """
        Tests the initialization of the FlowValidationError class with a field name and message.
        """
        exception = FlowValidationError("field1", "Test error message", None)
        self.assertEqual(exception.error_dict, {"field1": "Test error message"})

    def test_init_with_error_dict(self):
        """
        Tests the initialization of the FlowValidationError class with an error dictionary.
        """
        error_dict = {"field1": "Test error message", "field2": "Another error message"}
        exception = FlowValidationError(None, None, error_dict)
        self.assertEqual(exception.error_dict, error_dict)

    def test_raise_flow_validation_error(self):
        """
        Tests the raising of a FlowValidationError.
        """
        with self.assertRaises(FlowValidationError) as context:
            raise FlowValidationError("field1", "Test error message", None)
        self.assertEqual(context.exception.error_dict, {"field1": "Test error message"})
