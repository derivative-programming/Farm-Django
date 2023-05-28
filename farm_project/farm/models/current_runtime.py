import farm.models as models
import logging

class CurrentRuntime:

    @staticmethod
    def initialize():
        logging.debug('Models.CurrentRuntime.initialize() Start')
        models.Pac.initialize()
        ##endset
        
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
        logging.debug('Models.CurrentRuntime.initialize() End')