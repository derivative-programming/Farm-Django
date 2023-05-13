import factory
import uuid
from django.utils import timezone
from factory import Faker, SubFactory
from faker import Factory as FakerFactory
from api.models import Flavor
from faker import Faker
from datetime import timedelta
from .Pac import PacFactory
 
 
class FlavorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Flavor
 
    # flavor_id = factory.Sequence(lambda n: n)
    code = uuid.uuid4()
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = uuid.uuid4()
    last_update_user_id = uuid.uuid4()
    last_change_code = uuid.uuid4()
    description = factory.Faker('text', max_nb_chars=500)
    display_order = factory.Sequence(lambda n: n)
    is_active = True
    lookup_enum_name = factory.Faker('word')
    name = factory.Faker('word')
    pac = SubFactory(PacFactory)