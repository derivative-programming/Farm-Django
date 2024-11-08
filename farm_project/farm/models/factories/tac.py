# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from datetime import datetime, timezone
from farm.models import Tac
from farm.models.managers import TacEnum
from .pac import PacFactory #pac_id
class TacFactory(DjangoModelFactory):
    class Meta:
        model = Tac
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    description = Faker('sentence', nb_words=4)
    display_order = Faker('random_int')
    is_active = Faker('boolean')
    lookup_enum_name = Faker('sentence', nb_words=4)
    name = Faker('sentence', nb_words=4)
    pac = SubFactory(PacFactory) #pac_id


    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        items = Tac.objects.all()
        if len(items)>0:
            for item in items:
                if item.lookup_enum_name == 'Uknown':
                    items.remove(item)
        return random.choice(items)


