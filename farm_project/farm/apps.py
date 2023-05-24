from django.apps import AppConfig
import logging


class FarmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farm'
    
    def ready(self):  
        logging.debug('App initializing...')

        ### TODO create lookup records

