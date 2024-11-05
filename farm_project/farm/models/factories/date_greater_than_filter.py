# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from datetime import datetime, timezone
from farm.models import DateGreaterThanFilter
from farm.models.managers import DateGreaterThanFilterEnum
from .pac import PacFactory #pac_id
class DateGreaterThanFilterFactory(DjangoModelFactory):
    class Meta:
        model = DateGreaterThanFilter
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
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

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=true]Start  
    @classmethod
    def _create(cls, model_class, *args, **kwargs): 
        items = DateGreaterThanFilter.objects.all()
        if len(items)>0:
            for item in items:
                if item.lookup_enum_name == 'Uknown':
                    items.remove(item)
        return random.choice(items)
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=true]End
##GENTrainingBlock[caselookup]End
