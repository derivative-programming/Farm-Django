from django.db import models
from datetime import datetime, timezone
import uuid
from django.contrib import admin
class OrgApiKeyAdmin(admin.ModelAdmin):
    readonly_fields = ('org_api_key_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = (
        'org_api_key_id',
        'api_key_value',
        'created_by',
        'created_utc_date_time',
        'expiration_utc_date_time',
        'is_active',
        'is_temp_user_key',
        'name',
        'organization_id',
        'org_customer_id',
        'code',
        )
