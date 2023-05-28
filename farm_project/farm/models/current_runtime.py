import farm.models as models
import logging

class CurrentRuntime:

    @staticmethod
    def initialize_root_model():
        models.Pac.initialize()
#endset

    @staticmethod
    def initialize():
        logging.debug('Models.CurrentRuntime.initialize() Start')
        CurrentRuntime.initialize_root_model()
        CurrentRuntime.initialize_models()
        logging.debug('Models.CurrentRuntime.initialize() End')

    @staticmethod
    def initialize_models():
        logging.debug('Models.CurrentRuntime.initialize Models')
        
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
#endset
