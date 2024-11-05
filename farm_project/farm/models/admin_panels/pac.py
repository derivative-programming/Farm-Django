from django.db import models
from datetime import datetime, timezone
import datetime
import uuid 
from django.contrib import admin
class PacAdmin(admin.ModelAdmin):
    readonly_fields = ('pac_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = ( 
        'pac_id',
        'description',
        'display_order',
        'is_active',
        'lookup_enum_name',
        'name',
        'code', 
        )
