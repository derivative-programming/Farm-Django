from rest_framework import serializers

from api.models import Tac 

  
class TacSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tac
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',  
            'code'
            )