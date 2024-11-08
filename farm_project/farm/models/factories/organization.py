# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from datetime import datetime, timezone
from farm.models import Organization
from farm.models.managers import OrganizationEnum
from .tac import TacFactory #tac_id
class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    name = Faker('sentence', nb_words=4)
    tac = SubFactory(TacFactory) #tac_id




