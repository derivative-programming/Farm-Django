import factory
import uuid
from django.utils import timezone
from factory import Faker, SubFactory
from faker import Factory as FakerFactory
from .models import Pac, Tac
from faker import Faker
from datetime import timedelta
faker = FakerFactory.create()

class PacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pac

    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_udpate_utc_date_time = factory.LazyFunction(timezone.now)
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


class TacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tac

    tac_id = factory.Sequence(lambda n: n)
    code = uuid.uuid4()
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_udpate_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = uuid.uuid4()
    last_update_user_id = uuid.uuid4()
    last_change_code = uuid.uuid4()
    description = factory.Faker('text', max_nb_chars=500)
    display_order = factory.Sequence(lambda n: n)
    is_active = True
    lookup_enum_name = factory.Faker('word')
    name = factory.Faker('word')
    pac = SubFactory(PacFactory)