from django.db import models
from django.utils import timezone
import datetime
import uuid 
from django.contrib import admin
class DateGreaterThanFilterAdmin(admin.ModelAdmin):
    readonly_fields = ('date_greater_than_filter_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = ( 
        'date_greater_than_filter_id',
        'day_count',
        'description',
        'display_order',
        'is_active',
        'lookup_enum_name',
        'name',
        'pac_id',
        'code', 
        )
