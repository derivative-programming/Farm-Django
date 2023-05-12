from rest_framework import serializers

from api.models import Organization 
    
class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'name',
            'tac_id',  
            'code'
            )