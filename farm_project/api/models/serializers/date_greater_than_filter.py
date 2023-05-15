from rest_framework import serializers
from api.models import DateGreaterThanFilter 
class DateGreaterThanFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DateGreaterThanFilter
        fields = (
            'day_count',
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',
            'code'
            )
