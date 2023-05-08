from django.test import TestCase


from .models import TriStateFilter

from .models import Tac

from .models import Role

from .models import Plant

from .models import Pac

from .models import OrgCustomer

from .models import OrgApiKey

from .models import Organization

from .models import Land

from .models import Flavor

from .models import ErrorLog

from .models import DateGreaterThanFilter

from .models import CustomerRole

from .models import Customer 



class TriStateFilterTestCase(TestCase):
    def test_triStateFilter(self):
        self.assertEquals(
            TriStateFilter.objects.count(),
            0
        )
        TriStateFilter.objects.create() 
        self.assertEquals(
            TriStateFilter.objects.count(),
            1
        ) 

class TacTestCase(TestCase):
    def test_tac(self):
        self.assertEquals(
            Tac.objects.count(),
            0
        )
        Tac.objects.create() 
        self.assertEquals(
            Tac.objects.count(),
            1
        ) 

class RoleTestCase(TestCase):
    def test_role(self):
        self.assertEquals(
            Role.objects.count(),
            0
        )
        Role.objects.create() 
        self.assertEquals(
            Role.objects.count(),
            1
        ) 

class PlantTestCase(TestCase):
    def test_plant(self):
        self.assertEquals(
            Plant.objects.count(),
            0
        )
        Plant.objects.create() 
        self.assertEquals(
            Plant.objects.count(),
            1
        ) 

class PacTestCase(TestCase):
    def test_pac(self):
        self.assertEquals(
            Pac.objects.count(),
            0
        )
        Pac.objects.create() 
        self.assertEquals(
            Pac.objects.count(),
            1
        ) 

class OrgCustomerTestCase(TestCase):
    def test_orgCustomer(self):
        self.assertEquals(
            OrgCustomer.objects.count(),
            0
        )
        OrgCustomer.objects.create() 
        self.assertEquals(
            OrgCustomer.objects.count(),
            1
        ) 

class OrgApiKeyTestCase(TestCase):
    def test_orgApiKey(self):
        self.assertEquals(
            OrgApiKey.objects.count(),
            0
        )
        OrgApiKey.objects.create() 
        self.assertEquals(
            OrgApiKey.objects.count(),
            1
        ) 

class OrganizationTestCase(TestCase):
    def test_organization(self):
        self.assertEquals(
            Organization.objects.count(),
            0
        )
        Organization.objects.create() 
        self.assertEquals(
            Organization.objects.count(),
            1
        ) 

class LandTestCase(TestCase):
    def test_land(self):
        self.assertEquals(
            Land.objects.count(),
            0
        )
        Land.objects.create() 
        self.assertEquals(
            Land.objects.count(),
            1
        ) 

class FlavorTestCase(TestCase):
    def test_flavor(self):
        self.assertEquals(
            Flavor.objects.count(),
            0
        )
        Flavor.objects.create() 
        self.assertEquals(
            Flavor.objects.count(),
            1
        ) 

class ErrorLogTestCase(TestCase):
    def test_errorLog(self):
        self.assertEquals(
            ErrorLog.objects.count(),
            0
        )
        ErrorLog.objects.create() 
        self.assertEquals(
            ErrorLog.objects.count(),
            1
        ) 

class DateGreaterThanFilterTestCase(TestCase):
    def test_dateGreaterThanFilter(self):
        self.assertEquals(
            DateGreaterThanFilter.objects.count(),
            0
        )
        DateGreaterThanFilter.objects.create() 
        self.assertEquals(
            DateGreaterThanFilter.objects.count(),
            1
        ) 

class CustomerRoleTestCase(TestCase):
    def test_customerRole(self):
        self.assertEquals(
            CustomerRole.objects.count(),
            0
        )
        CustomerRole.objects.create() 
        self.assertEquals(
            CustomerRole.objects.count(),
            1
        ) 

class CustomerTestCase(TestCase):
    def test_customer(self):
        self.assertEquals(
            Customer.objects.count(),
            0
        )
        Customer.objects.create() 
        self.assertEquals(
            Customer.objects.count(),
            1
        )  