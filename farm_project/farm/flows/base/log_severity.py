# flows/base/log_severity.py
"""
This module initializes the log severity used in the project.
"""
from enum import Enum

class LogSeverity(Enum):
    """
    This class initializes the log severity used in the project.
    """
    error_occurred = 0
    warning = 1
    information_low_detail = 2
    information_mid_detail = 3
    information_high_detail = 4
