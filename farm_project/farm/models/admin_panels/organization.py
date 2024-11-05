from django.db import models
from datetime import datetime, timezone
from django.contrib import admin
class OrganizationAdmin(admin.ModelAdmin):
    readonly_fields = ('organization_id','code','insert_utc_date_time','last_update_utc_date_time','insert_user_id','last_update_user_id','last_change_code')
    list_display = (
        'organization_id',
        'name',
        'tac_id',
        'code',
        )
