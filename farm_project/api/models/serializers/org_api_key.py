from rest_framework import serializers
from api.models import OrgApiKey 
class OrgApiKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrgApiKey
        fields = (
            'api_key_value',
            'created_by',
            'created_utc_date_time',
            'expiration_utc_date_time',
            'is_active',
            'is_temp_user_key',
            'name',
            'organization_id',
            'org_customer_id',
            'code'
            )
