from rest_framework import serializers
from api.models import Pac 
class PacSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pac
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'code'
            )
