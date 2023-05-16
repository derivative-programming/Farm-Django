
from datetime import date, datetime

class TypeConversion:

    @staticmethod
    def get_default_date():
        return date(1753,1,1)

    @staticmethod
    def get_default_date_time():
        return datetime(1752,1,1,0,0) 