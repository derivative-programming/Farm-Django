from django.db import models
from django.utils import timezone
import datetime
import uuid 
from django.contrib import admin


class OrgCustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('org_customer_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = (  
        'org_customer_id',
        'customer_id',
        'organization_id',
        'code', 
        )
