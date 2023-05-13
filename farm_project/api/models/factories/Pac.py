import factory
import uuid
from django.utils import timezone
from factory import Faker, SubFactory
from faker import Factory as FakerFactory
from api.models import Pac 
from faker import Faker
from datetime import timedelta


class PacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pac
     
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    description = factory.Faker('text', max_nb_chars=500)
    display_order = factory.Sequence(lambda n: n)
    is_active = factory.Faker('boolean')
    lookup_enum_name = factory.Faker('text', max_nb_chars=50)
    name = factory.Faker('text', max_nb_chars=100)

    @classmethod
    def create_batch(cls, size, **kwargs):
        return [cls() for _ in range(size)]