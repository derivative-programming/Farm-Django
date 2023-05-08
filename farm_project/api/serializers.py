from rest_framework import serializers

from . import models 

 

class TriStateFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TriStateFilter
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',
            'state_int_value',  
            'code'
            )
class TacSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tac
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',  
            'code'
            )
class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',  
            'code'
            )
class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Plant
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
class PacSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Pac
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',  
            'code'
            )
class OrgCustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OrgCustomer
        fields = (
            'customer_id',
            'email',
            'organization_id',  
            'code'
            )
class OrgApiKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OrgApiKey
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
class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organization
        fields = (
            'name',
            'tac_id',  
            'code'
            )
class LandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Land
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',  
            'code'
            )
class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Flavor
        fields = (
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',  
            'code'
            )
class ErrorLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ErrorLog
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
class DateGreaterThanFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DateGreaterThanFilter
        fields = (
            'day_count',
            'description',
            'display_order',
            'is_active',
            'lookup_enum_name',
            'name',
            'pac_id',  
            'code'
            )
class CustomerRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomerRole
        fields = (
            'customer_id',
            'is_placeholder',
            'placeholder',
            'role_id',  
            'code'
            )
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customer
        fields = (
            'active_organization_id',
            'email',
            'email_confirmed_utc_date_time',
            'first_name',
            'forgot_password_key_expiration_utc_date_time',
            'forgot_password_key_value',
            'fs_user_code_value',
            'is_active',
            'is_email_allowed',
            'is_email_confirmed',
            'is_email_marketing_allowed',
            'is_locked',
            'is_multiple_organizations_allowed',
            'is_verbose_logging_forced',
            'last_login_utc_date_time',
            'last_name',
            'password',
            'phone',
            'province',
            'registration_utc_date_time',
            'tac_id',
            'utc_offset_in_minutes',
            'zip',  
            'code'
            ) 