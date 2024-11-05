# flows/base/base_flow.py
"""
Base flow for all flows.
"""
import logging

from farm.helpers import SessionContext

from .flow_validation_error import FlowValidationError
from .log_severity import LogSeverity


class BaseFlow():
    """
    Base flow for all flows.
    """
    __flow_name = ""
    queued_validation_errors:dict
    _session_context:SessionContext

    def __init__(self, flow_name:str, session_context:SessionContext):
        """
        Initializes the base flow for all flows.
        """
        self._session_context = session_context
        self.__flow_name = flow_name
        self.queued_validation_errors = dict()

    def _add_validation_error(self, message:str):
        """
        Adds a validation error.
        """
        self._add_field_validation_error("", message)

    def _add_field_validation_error(self, field_name:str = "", message:str = ""):
        """
        Adds a field validation error.
        """
        if field_name in self.queued_validation_errors:
            current_val = self.queued_validation_errors[field_name]
            self.queued_validation_errors[field_name] = current_val + ',' + message
        else:
            self.queued_validation_errors[field_name] = message


    def _throw_validation_error(self, message:str):
        """
        Throws a validation error.
        """
        self._throw_field_validation_error("", message)

    def _throw_field_validation_error(self, field_name:str, message:str):
        """
        Throws a field validation error.
        """
        raise FlowValidationError(field_name,message,None)


    def _throw_queued_validation_errors(self):
        """
        Throws queued validation errors.
        """
        if len(self.queued_validation_errors) > 0:
            raise FlowValidationError(None,None,self.queued_validation_errors)

    def _log_exception(self, ex:Exception):
        """
        Logs an exception.
        """
        self._log_message_and_severity(LogSeverity.error_occurred,str(ex))

    def _log_message_and_severity(self, log_severity:int, message:str):
        """
        Logs a message and severity.
        """

        log_message = self.__flow_name + " " + message

        match log_severity:
            case LogSeverity.error_occurred:
                logging.error(log_message)
            case LogSeverity.warning:
                logging.critical(log_message)
            case LogSeverity.information_low_detail:
                logging.warning(log_message)
            case LogSeverity.information_mid_detail:
                logging.info(log_message)
            case LogSeverity.information_high_detail:
                logging.debug(log_message)

    def _log_message(self, message:str):
        """
        Logs a message.
        """
        self._log_message_and_severity(LogSeverity.information_high_detail,message)
