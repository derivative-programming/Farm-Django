from rest_framework import serializers
from farm.models import Organization
class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'name',
            'tac_id',
            'code'
            )
