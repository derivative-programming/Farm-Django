from rest_framework import serializers
from farm.models import Land 
class LandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Land
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',
            'code'
            )
