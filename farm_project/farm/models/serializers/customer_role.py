from rest_framework import serializers
from farm.models import CustomerRole
class CustomerRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerRole
        fields = (
            'customer_id',
            'is_placeholder',
            'placeholder',
            'role_id',
            'code'
            )
