from django.apps import AppConfig
import logging


class FarmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farm'
    
    def ready(self):  
        logging.debug('App initializing...')

        import farm.models as models
        try:
                
            models.Pac.initialize();
    ##endset
            ### TODO create lookup records
            models.Customer.initialize();
            models.CustomerRole.initialize();
            models.DateGreaterThanFilter.initialize();
            models.ErrorLog.initialize();
            models.Flavor.initialize();
            models.Land.initialize();
            models.Organization.initialize();
            models.OrgApiKey.initialize();
            models.OrgCustomer.initialize();
            models.Pac.initialize();
            models.Plant.initialize();
            models.Role.initialize();
            models.Tac.initialize();
            models.TriStateFilter.initialize(); 
    ##endset
        except Exception:
            pass
        logging.debug('App initialization complete')

