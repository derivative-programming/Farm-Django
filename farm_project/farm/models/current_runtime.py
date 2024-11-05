# models/current_runtime.py
"""
This module defines the CurrentRuntime class, which is responsible for initializing
various models
"""
import logging

import farm.models as models

class CurrentRuntime:
    """
    This class is responsible for initializing various models
    """

    @staticmethod
    def initialize_root_model():
        """
        Initializes the root model
        """
        models.Pac.initialize()
#endset

    @staticmethod
    def initialize():
        """
        Initializes all the models in the project
        """
        logging.debug('Models.CurrentRuntime.initialize() Start')
        CurrentRuntime.initialize_root_model()
        CurrentRuntime.initialize_models()
        logging.debug('Models.CurrentRuntime.initialize() End')

    @staticmethod
    def initialize_models():
        """
        Initializes all the models in the project
        """
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
