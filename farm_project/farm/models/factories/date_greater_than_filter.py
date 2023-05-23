# farm/models/factories.py
import uuid
import factory
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from farm.models import DateGreaterThanFilter
from .pac import PacFactory #pac_id
class DateGreaterThanFilterFactory(DjangoModelFactory):
    class Meta:
        model = DateGreaterThanFilter
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    day_count = Faker('random_int')
    description = Faker('sentence', nb_words=4)
    display_order = Faker('random_int')
    is_active = Faker('boolean')
    lookup_enum_name = Faker('sentence', nb_words=4)
    name = Faker('sentence', nb_words=4)
    pac = SubFactory(PacFactory) #pac_id