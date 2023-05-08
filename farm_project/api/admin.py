from django.contrib import admin
from . import models 
 


admin.site.register(models.TriStateFilter)

admin.site.register(models.Tac)

admin.site.register(models.Role)

admin.site.register(models.Plant)

admin.site.register(models.Pac)

admin.site.register(models.OrgCustomer)

admin.site.register(models.OrgApiKey)

admin.site.register(models.Organization)

admin.site.register(models.Land)

admin.site.register(models.Flavor)

admin.site.register(models.ErrorLog)

admin.site.register(models.DateGreaterThanFilter)

admin.site.register(models.CustomerRole)

admin.site.register(models.Customer)
 