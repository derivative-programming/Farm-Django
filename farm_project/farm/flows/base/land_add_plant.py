# flows/base/land_add_plant.py
"""
Base flow for land_add_plant.
"""
import uuid
from farm.models import Land
from .base_flow import BaseFlow
from farm.flows.base import LogSeverity
from farm.helpers import SessionContext
from decimal import Decimal
from datetime import date, datetime
from farm.helpers import TypeConversion
import farm.flows.constants.land_add_plant as FlowConstants
import farm.models as farm_models

class BaseFlowLandAddPlant(BaseFlow):
    """
    Base flow for land_add_plant.
    """
    def __init__(self, session_context:SessionContext):
        """
        Initializes the base flow for land_add_plant.
        """
        super(BaseFlowLandAddPlant, self).__init__(
            "LandAddPlant",
            session_context,
            )


    def _process_validation_rules(self,
            land: Land,
            request_flavor_code: uuid.UUID = "",
            request_other_flavor:str = "",
            request_some_int_val:int = 0,
            request_some_big_int_val:int = 0,
            request_some_bit_val:bool = False,
            request_is_edit_allowed:bool = False,
            request_is_delete_allowed:bool = False,
            request_some_float_val:float = 0,
            request_some_decimal_val:Decimal = 0,
            request_some_utc_date_time_val:datetime = TypeConversion.get_default_date_time(),
            request_some_date_val:date = TypeConversion.get_default_date(),
            request_some_money_val:Decimal = 0,
            request_some_n_var_char_val:str = "",
            request_some_var_char_val:str = "",
            request_some_text_val:str = "",
            request_some_phone_number:str = "",
            request_some_email_address:str = "",
            request_sample_image_upload_file:str = "",
        ):
        """
        Processes the validation rules for land_add_plant.
        """
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")

        if request_flavor_code == "" and FlowConstants.param_request_flavor_code_isRequired == True:
            self._add_field_validation_error("requestFlavorCode","Please select a Flavor")

        if request_other_flavor == "" and FlowConstants.param_request_other_flavor_isRequired == True:
            self._add_field_validation_error("requestOtherFlavor","Please enter a Other Flavor")

        if request_some_int_val == 0 and FlowConstants.param_request_some_int_val_isRequired == True:
            self._add_field_validation_error("requestSomeIntVal","Please enter a Some Int Val")

        if request_some_big_int_val == 0 and FlowConstants.param_request_some_big_int_val_isRequired == True:
            self._add_field_validation_error("requestSomeBigIntVal","Please enter a Some Big Int Val")

        if request_some_bit_val == None and FlowConstants.param_request_some_bit_val_isRequired == True:
            self._add_field_validation_error("requestSomeBitVal","Please enter a Some Bit Val")

        if request_is_edit_allowed == None and FlowConstants.param_request_is_edit_allowed_isRequired == True:
            self._add_field_validation_error("requestIsEditAllowed","Please enter a Is Edit Allowed")

        if request_is_delete_allowed == None and FlowConstants.param_request_is_delete_allowed_isRequired == True:
            self._add_field_validation_error("requestIsDeleteAllowed","Please enter a Is Delete Allowed")

        if request_some_float_val == 0 and FlowConstants.param_request_some_float_val_isRequired == True:
            self._add_field_validation_error("requestSomeFloatVal","Please enter a Some Float Val")

        if request_some_decimal_val == 0 and FlowConstants.param_request_some_decimal_val_isRequired == True:
            self._add_field_validation_error("requestSomeDecimalVal","Please enter a Some Decimal Val")

        if request_some_utc_date_time_val == "" and FlowConstants.param_request_some_utc_date_time_val_isRequired == True:
            self._add_field_validation_error("requestSomeUTCDateTimeVal","Please enter a Some UTC Date Time Val")

        if request_some_date_val == "" and FlowConstants.param_request_some_date_val_isRequired == True:
            self._add_field_validation_error("requestSomeDateVal","Please enter a Some Date Val")

        if request_some_money_val == "" and FlowConstants.param_request_some_money_val_isRequired == True:
            self._add_field_validation_error("requestSomeMoneyVal","Please enter a Some Money Val")

        if request_some_n_var_char_val == "" and FlowConstants.param_request_some_n_var_char_val_isRequired == True:
            self._add_field_validation_error("requestSomeNVarCharVal","Please enter a Some N Var Char Val")

        if request_some_var_char_val == "" and FlowConstants.param_request_some_var_char_val_isRequired == True:
            self._add_field_validation_error("requestSomeVarCharVal","Please enter a Some Var Char Val")

        if request_some_text_val == "" and FlowConstants.param_request_some_text_val_isRequired == True:
            self._add_field_validation_error("requestSomeTextVal","Please enter a Some Text Val")

        if request_some_phone_number == "" and FlowConstants.param_request_some_phone_number_isRequired == True:
            self._add_field_validation_error("requestSomePhoneNumber","Please enter a Some Phone Number")

        if request_some_email_address == "" and FlowConstants.param_request_some_email_address_isRequired == True:
            self._add_field_validation_error("requestSomeEmailAddress","Please enter a Some Email Address")

        if request_sample_image_upload_file == "" and FlowConstants.param_request_sample_image_upload_file_isRequired == True:
            self._add_field_validation_error("requestSampleImageUploadFile","Please enter a image file")



        self._process_security_rules(land)





    def _process_security_rules(self,
        land: Land,
        ):
        """
        Processes the security rules for land_add_plant.
        """
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")

        customerCodeMatchRequired = False

        role_required = "User"

        if len(role_required) > 0:
            if role_required not in self._session_context.role_name_csv:
                self._add_validation_error("Unautorized access. " + role_required + " role not found.")


        if FlowConstants.calculatedIsRowLevelCustomerSecurityUsed == True:
            customerCodeMatchRequired = True
        if FlowConstants.calculatedIsRowLevelOrganizationSecurityUsed == True:
            customerCodeMatchRequired = True
        if FlowConstants.calculatedIsRowLevelOrgCustomerSecurityUsed == True:
            customerCodeMatchRequired = True

        if customerCodeMatchRequired == True:

            val = True

            item = land

            while val:
                if item.get_object_name() == "pac":
                    val = False

##GENTrainingBlock[caseFlowLogic_calculatedIsRowLevelOrgCustomerSecurityUsed]Start
##GENLearn[calculatedIsRowLevelOrgCustomerSecurityUsed=true]Start
                if FlowConstants.calculatedIsRowLevelOrgCustomerSecurityUsed == True:
                    if item.get_object_name() == "org_customer":
                        item = item.customer
##GENLearn[calculatedIsRowLevelOrgCustomerSecurityUsed=true]End
##GENTrainingBlock[caseFlowLogic_calculatedIsRowLevelOrgCustomerSecurityUsed]End

##GENTrainingBlock[caseFlowLogic_calculatedIsRowLevelCustomerSecurityUsed]Start
##GENLearn[calculatedIsRowLevelCustomerSecurityUsed=true]Start
                if FlowConstants.calculatedIsRowLevelCustomerSecurityUsed == True:
                    if item.get_object_name() == "customer":
                        if item.code != self._session_context.customer_code:
                            self._add_validation_error("Unautorized access.  Invalid User.")
##GENLearn[calculatedIsRowLevelCustomerSecurityUsed=true]End
##GENTrainingBlock[caseFlowLogic_calculatedIsRowLevelCustomerSecurityUsed]End

##GENTrainingBlock[caseFlowLogic_calculatedIsRowLevelOrganizationSecurityUsed]Start
##GENLearn[calculatedIsRowLevelOrganizationSecurityUsed=true]Start
                if FlowConstants.calculatedIsRowLevelOrganizationSecurityUsed == True:
                    if item.get_object_name() == "organization":
                        customer = farm_models.Customer.objects.from_code(self._session_context.customer_code)
                        org_customers = farm_models.OrgCustomer.objects.filter(organization_id=item.organization_id, customer_id=customer.customer_id)
                        if org_customers.count() == 0:
                            self._add_validation_error("Unautorized access. Invalid user in organization.")
##GENLearn[calculatedIsRowLevelOrganizationSecurityUsed=true]End
##GENTrainingBlock[caseFlowLogic_calculatedIsRowLevelOrganizationSecurityUsed]End


                item = item.get_parent_object()
