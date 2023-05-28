# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from farm.models import Role
from farm.models.managers import RoleEnum
from .pac import PacFactory #pac_id
class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Role
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
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
        items = Role.objects.all()
        if len(items)>0:
            for item in items:
                if item.lookup_enum_name == 'Uknown':
                    items.remove(item)
        return random.choice(items)


