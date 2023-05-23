# farm/models/factories.py
import uuid
import factory
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from farm.models import Organization
from .tac import TacFactory #tac_id
class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    name = Faker('sentence', nb_words=4)
    tac = SubFactory(TacFactory) #tac_id
