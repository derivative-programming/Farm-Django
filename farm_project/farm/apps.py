# apps.py
"""
configures the app
"""
import logging
from django.apps import AppConfig

class FarmConfig(AppConfig):
    """
    configures the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farm'

    def ready(self):
        """
        Initializes the app
        """
        logging.debug('App initializing...')

        import farm.models as models
        try:

            models.Pac.initialize()
    ##endset
            ### TODO create lookup records
            models.Customer.initialize()
            models.CustomerRole.initialize()
            models.DateGreaterThanFilter.initialize()
            models.ErrorLog.initialize()
            models.Flavor.initialize()
            models.Land.initialize()
            models.Organization.initialize()
            models.OrgApiKey.initialize()
            models.OrgCustomer.initialize()
            models.Pac.initialize()
            models.Plant.initialize()
            models.Role.initialize()
            models.Tac.initialize()
            models.TriStateFilter.initialize()
    ##endset
        except Exception:
            pass
        logging.debug('App initialization complete')
