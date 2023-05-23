from rest_framework import serializers
from farm.models import TriStateFilter 
class TriStateFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TriStateFilter
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',
            'state_int_value',
            'code'
            )
