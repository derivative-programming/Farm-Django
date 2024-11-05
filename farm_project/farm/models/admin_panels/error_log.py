from django.db import models
from datetime import datetime, timezone
import datetime
import uuid 
from django.contrib import admin
class ErrorLogAdmin(admin.ModelAdmin):
    readonly_fields = ('error_log_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = ( 
        'error_log_id',
        'browser_code',
        'context_code',
        'created_utc_date_time',
        'description',
        'is_client_side_error',
        'is_resolved',
        'pac_id',
        'url',
        'code', 
        )
