from django.test import TestCase
from api.models import DateGreaterThanFilter 
 



class DateGreaterThanFilterTestCase(TestCase):
    def test_date_greater_than_filter(self):
        self.assertEquals(
            DateGreaterThanFilter.objects.count(),
            0
        )
        DateGreaterThanFilter.objects.create() 
        self.assertEquals(
            DateGreaterThanFilter.objects.count(),
            1
        ) 