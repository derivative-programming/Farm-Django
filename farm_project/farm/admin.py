from django.contrib import admin
from farm import models
from farm.models import admin_panels




admin.site.register(models.TriStateFilter,admin_panels.TriStateFilterAdmin)
admin.site.register(models.Tac,admin_panels.TacAdmin)
admin.site.register(models.Role,admin_panels.RoleAdmin)
admin.site.register(models.Plant,admin_panels.PlantAdmin)
admin.site.register(models.Pac,admin_panels.PacAdmin)
admin.site.register(models.OrgCustomer,admin_panels.OrgCustomerAdmin)
admin.site.register(models.OrgApiKey,admin_panels.OrgApiKeyAdmin)
admin.site.register(models.Organization,admin_panels.OrganizationAdmin)
admin.site.register(models.land.Land,admin_panels.LandAdmin)
admin.site.register(models.flavor.Flavor,admin_panels.FlavorAdmin)
admin.site.register(models.ErrorLog,admin_panels.ErrorLogAdmin)
admin.site.register(models.DateGreaterThanFilter,admin_panels.DateGreaterThanFilterAdmin)
admin.site.register(models.CustomerRole,admin_panels.CustomerRoleAdmin)
admin.site.register(models.Customer,admin_panels.CustomerAdmin)
