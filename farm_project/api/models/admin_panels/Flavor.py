from django.db import models
from django.utils import timezone
import datetime
import uuid
from django.contrib import admin



class FlavorAdmin(admin.ModelAdmin):
    readonly_fields = ('flavor_id','code','insert_utc_date_time','last_udpate_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = (  
        'flavor_id',
        'description',
        'display_order',
        'is_active',
        'lookup_enum_name',
        'name',
        'pac_id', 
        'code', 
        )