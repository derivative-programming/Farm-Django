# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from datetime import datetime, timezone
from farm.models import ErrorLog
from farm.models.managers import ErrorLogEnum
from .pac import PacFactory #pac_id
class ErrorLogFactory(DjangoModelFactory):
    class Meta:
        model = ErrorLog
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    browser_code = factory.LazyFunction(uuid.uuid4)
    context_code = factory.LazyFunction(uuid.uuid4)
    created_utc_date_time = Faker('date_time', tzinfo=timezone.utc)
    description = Faker('sentence', nb_words=4)
    is_client_side_error = Faker('boolean')
    is_resolved = Faker('boolean')
    pac = SubFactory(PacFactory) #pac_id
    url = Faker('sentence', nb_words=4)




