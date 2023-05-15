from django.db import models
from django.utils import timezone
import datetime
import uuid 
from django.contrib import admin
class CustomerRoleAdmin(admin.ModelAdmin):
    readonly_fields = ('customer_role_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = ( 
        'customer_role_id',
        'customer_id',
        'is_placeholder',
        'placeholder',
        'role_id',
        'code', 
        )
