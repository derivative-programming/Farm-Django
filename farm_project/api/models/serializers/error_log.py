from rest_framework import serializers
from api.models import ErrorLog 
class ErrorLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ErrorLog
        fields = (
            'browser_code',
            'context_code',
            'created_utc_date_time',
            'description',
            'is_client_side_error',
            'is_resolved',
            'pac_id',
            'url',
            'code'
            )
