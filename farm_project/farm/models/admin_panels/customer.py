from django.db import models
from datetime import datetime, timezone
import datetime
import uuid 
from django.contrib import admin
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('customer_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = ( 
        'customer_id',
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
        'code', 
        )
