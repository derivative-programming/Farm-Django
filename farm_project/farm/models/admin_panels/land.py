from django.db import models
from datetime import datetime, timezone
import datetime
import uuid 
from django.contrib import admin
class LandAdmin(admin.ModelAdmin):
    readonly_fields = ('land_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = ( 
        'land_id',
        'description',
        'display_order',
        'is_active',
        'lookup_enum_name',
        'name',
        'pac_id',
        'code', 
        )
