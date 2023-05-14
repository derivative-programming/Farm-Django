import uuid
from django.utils import timezone
from factory import Faker, SubFactory, Sequence, LazyFunction
from factory.django import DjangoModelFactory 
from api.models import DateGreaterThanFilter 
from datetime import timedelta
from .Pac import PacFactory
 
  
class DateGreaterThanFilterFactory(DjangoModelFactory):
    class Meta:
        model = DateGreaterThanFilter
 
    # date_greater_than_filter_id = factory.Sequence(lambda n: n)
    code = LazyFunction(uuid.uuid4)
    insert_utc_date_time = Faker('past_datetime', start_date="-30d")
    last_update_utc_date_time = Faker('past_datetime', start_date="-30d")
    insert_user_id = Faker('uuid4')
    last_update_user_id = Faker('uuid4')
    last_change_code = Faker('uuid4')
    description = Faker('text', max_nb_chars=500)
    display_order = Sequence(lambda n: n)
    is_active = True
    lookup_enum_name = Faker('word')
    name = Faker('word')
    pac = SubFactory(PacFactory)