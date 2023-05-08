from django.test import TestCase
from . import models 
 



class TriStateFilterTestCase(TestCase):
    def test_triStateFilter(self):
        self.assertEquals(
            models.TriStateFilter.objects.count(),
            0
        )
        models.TriStateFilter.objects.create() 
        self.assertEquals(
            models.TriStateFilter.objects.count(),
            1
        ) 

class TacTestCase(TestCase):
    def test_tac(self):
        self.assertEquals(
            models.Tac.objects.count(),
            0
        )
        models.Tac.objects.create() 
        self.assertEquals(
            models.Tac.objects.count(),
            1
        ) 

class RoleTestCase(TestCase):
    def test_role(self):
        self.assertEquals(
            models.Role.objects.count(),
            0
        )
        models.Role.objects.create() 
        self.assertEquals(
            models.Role.objects.count(),
            1
        ) 

class PlantTestCase(TestCase):
    def test_plant(self):
        self.assertEquals(
            models.Plant.objects.count(),
            0
        )
        models.Plant.objects.create() 
        self.assertEquals(
            models.Plant.objects.count(),
            1
        ) 

class PacTestCase(TestCase):
    def test_pac(self):
        self.assertEquals(
            models.Pac.objects.count(),
            0
        )
        models.Pac.objects.create() 
        self.assertEquals(
            models.Pac.objects.count(),
            1
        ) 

class OrgCustomerTestCase(TestCase):
    def test_orgCustomer(self):
        self.assertEquals(
            models.OrgCustomer.objects.count(),
            0
        )
        models.OrgCustomer.objects.create() 
        self.assertEquals(
            models.OrgCustomer.objects.count(),
            1
        ) 

class OrgApiKeyTestCase(TestCase):
    def test_orgApiKey(self):
        self.assertEquals(
            models.OrgApiKey.objects.count(),
            0
        )
        models.OrgApiKey.objects.create() 
        self.assertEquals(
            models.OrgApiKey.objects.count(),
            1
        ) 

class OrganizationTestCase(TestCase):
    def test_organization(self):
        self.assertEquals(
            models.Organization.objects.count(),
            0
        )
        models.Organization.objects.create() 
        self.assertEquals(
            models.Organization.objects.count(),
            1
        ) 

class LandTestCase(TestCase):
    def test_land(self):
        self.assertEquals(
            models.Land.objects.count(),
            0
        )
        models.Land.objects.create() 
        self.assertEquals(
            models.Land.objects.count(),
            1
        ) 

class FlavorTestCase(TestCase):
    def test_flavor(self):
        self.assertEquals(
            models.Flavor.objects.count(),
            0
        )
        models.Flavor.objects.create() 
        self.assertEquals(
            models.Flavor.objects.count(),
            1
        ) 

class ErrorLogTestCase(TestCase):
    def test_errorLog(self):
        self.assertEquals(
            models.ErrorLog.objects.count(),
            0
        )
        models.ErrorLog.objects.create() 
        self.assertEquals(
            models.ErrorLog.objects.count(),
            1
        ) 

class DateGreaterThanFilterTestCase(TestCase):
    def test_dateGreaterThanFilter(self):
        self.assertEquals(
            models.DateGreaterThanFilter.objects.count(),
            0
        )
        models.DateGreaterThanFilter.objects.create() 
        self.assertEquals(
            models.DateGreaterThanFilter.objects.count(),
            1
        ) 

class CustomerRoleTestCase(TestCase):
    def test_customerRole(self):
        self.assertEquals(
            models.CustomerRole.objects.count(),
            0
        )
        models.CustomerRole.objects.create() 
        self.assertEquals(
            models.CustomerRole.objects.count(),
            1
        ) 

class CustomerTestCase(TestCase):
    def test_customer(self):
        self.assertEquals(
            models.Customer.objects.count(),
            0
        )
        models.Customer.objects.create() 
        self.assertEquals(
            models.Customer.objects.count(),
            1
        )  