# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from datetime import datetime, timezone
from farm.models import Pac
from farm.models.managers import PacEnum

class PacFactory(DjangoModelFactory):
    class Meta:
        model = Pac
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

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=false]Start  
    @classmethod
    def create(cls, **kwargs):
        pac = Pac.objects.from_enum(enum_val=PacEnum.Unknown)
        return pac
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=false]End
##GENTrainingBlock[caselookup]End
