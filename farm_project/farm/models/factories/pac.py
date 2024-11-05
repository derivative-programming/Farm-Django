# farm/models/factories.py
"""
Factory module for Pac model
"""
import random
import uuid
from datetime import datetime, timezone

import factory
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from farm.models import Pac
from farm.models.managers import PacEnum


class PacFactory(DjangoModelFactory):
    """
    Factory class for Pac model
    """
    class Meta:
        """
        Meta class for PacFactory
        """
        model = Pac
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    description: str = Faker('sentence', nb_words=4) # type: ignore
    display_order: int = Faker('random_int') # type: ignore
    is_active: bool = Faker('boolean') # type: ignore
    lookup_enum_name: str = Faker('sentence', nb_words=4) # type: ignore
    name: str = Faker('sentence', nb_words=4) # type: ignore

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=false]Start
    @classmethod
    def create(cls, **kwargs):
        """
        Create a Pac object
        """
        pac = Pac.objects.from_enum(enum_val=PacEnum.Unknown)
        return pac
##GENLearn[isLookup=true,calculatedIsParentObjectAvailable=false]End
##GENTrainingBlock[caselookup]End
