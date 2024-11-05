from rest_framework import serializers
from farm.models import OrgCustomer
class OrgCustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrgCustomer
        fields = (
            'customer_id',
            'email',
            'organization_id',
            'code'
            )
