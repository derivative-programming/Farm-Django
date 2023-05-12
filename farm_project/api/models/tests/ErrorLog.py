from django.test import TestCase
from api.models import ErrorLog 
 



class ErrorLogTestCase(TestCase):
    def test_error_log(self):
        self.assertEquals(
            ErrorLog.objects.count(),
            0
        )
        ErrorLog.objects.create() 
        self.assertEquals(
            ErrorLog.objects.count(),
            1
        ) 