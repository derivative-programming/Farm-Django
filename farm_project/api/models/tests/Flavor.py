from django.test import TestCase
from api.models import Flavor 
from api.models.factories.Flavor import FlavorFactory


class FlavorTestCase(TestCase):
    def setUp(self):
        Flavor.objects.all().delete()

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
        # create a Flavor object with default attributes
        flavor = FlavorFactory.create()
        # assert that the object was created successfully
        self.assertIsInstance(flavor, Flavor)
        self.assertIsNotNone(flavor.code)
        self.assertIsNotNone(flavor.insert_user_id)
        self.assertIsNotNone(flavor.last_update_user_id)
        self.assertIsNotNone(flavor.description)
        self.assertIsNotNone(flavor.display_order)
        self.assertIsNotNone(flavor.is_active)
        self.assertIsNotNone(flavor.lookup_enum_name)
        self.assertIsNotNone(flavor.name)
        self.assertIsNotNone(flavor.pac)