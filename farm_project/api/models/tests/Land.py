from django.test import TestCase
from api.models import Land 
from api.models.factories.Land import LandFactory


class LandTestCase(TestCase):
    def setUp(self):
        Land.objects.all().delete()

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
        # create a Land object with default attributes
        land = LandFactory.create()
        # assert that the object was created successfully
        self.assertIsInstance(land, Land)
        self.assertIsNotNone(land.code)
        self.assertIsNotNone(land.insert_user_id)
        self.assertIsNotNone(land.last_update_user_id)
        self.assertIsNotNone(land.description)
        self.assertIsNotNone(land.display_order)
        self.assertIsNotNone(land.is_active)
        self.assertIsNotNone(land.lookup_enum_name)
        self.assertIsNotNone(land.name)
        self.assertIsNotNone(land.pac)