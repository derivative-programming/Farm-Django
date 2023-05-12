from rest_framework import serializers

from api.models import Plant 

    
class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = (
            'flavor_id',
            'is_delete_allowed',
            'is_edit_allowed',
            'land_id',
            'other_flavor',
            'some_big_int_val',
            'some_bit_val',
            'some_date_val',
            'some_decimal_val',
            'some_email_address',
            'some_float_val',
            'some_int_val',
            'some_money_val',
            'some_n_var_char_val',
            'some_phone_number',
            'some_text_val',
            'some_uniqueidentifier_val',
            'some_utc_date_time_val',
            'some_var_char_val',  
            'code'
            )