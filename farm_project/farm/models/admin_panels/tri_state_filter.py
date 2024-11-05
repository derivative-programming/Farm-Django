from django.db import models
from datetime import datetime, timezone
import uuid
from django.contrib import admin
class TriStateFilterAdmin(admin.ModelAdmin):
    readonly_fields = ('tri_state_filter_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = (
        'tri_state_filter_id',
        'description',
        'display_order',
        'is_active',
        'lookup_enum_name',
        'name',
        'pac_id',
        'state_int_value',
        'code',
        )
