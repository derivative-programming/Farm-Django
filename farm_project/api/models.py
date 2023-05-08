from django.db import models
from django.utils import timezone
import datetime
import uuid



class Pac(models.Model):
    pac_id =  models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time = models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    description = models.TextField(max_length=500) 
    display_order = models.IntegerField(null=True) 
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=100)  

    def __str__(self):
        return str(self.code)

class TriStateFilter(models.Model):
    tri_state_filter_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    description = models.TextField(max_length=500) 
    display_order = models.IntegerField(null=True) 
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=100)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='tri_state_filter_list', on_delete=models.SET_NULL, blank=True, null=True) 
    state_int_value = models.IntegerField(null=True)
	  

    def __str__(self):
        return str(self.code)

class Tac(models.Model):
    tac_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    description = models.TextField(max_length=500)	
    display_order = models.IntegerField(null=True)	
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=100)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='tac_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    description = models.TextField(max_length=200)	
    display_order = models.IntegerField(null=True)	
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=50)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='role_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)
    
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time = models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)		
    active_organization_id = models.IntegerField(null=True)	
    email = models.TextField(max_length=100)
    email_confirmed_utc_date_time = models.DateTimeField(null=True)
    first_name = models.TextField(max_length=200)
    forgot_password_key_expiration_utc_date_time = models.DateTimeField(null=True)
    forgot_password_key_value = models.TextField(max_length=1000)
    fs_user_code_value = models.UUIDField(null=True)
    is_active = models.BooleanField(null=True)
    is_email_allowed = models.BooleanField(null=True)
    is_email_confirmed = models.BooleanField(null=True)
    is_email_marketing_allowed = models.BooleanField(null=True)
    is_locked = models.BooleanField(null=True)
    is_multiple_organizations_allowed = models.BooleanField(null=True)
    is_verbose_logging_forced = models.BooleanField(null=True)
    last_login_utc_date_time = models.DateTimeField(null=True)
    last_name = models.TextField(max_length=200)
    password = models.TextField(max_length=100)
    phone = models.TextField(max_length=50)
    province = models.TextField(max_length=50)
    registration_utc_date_time = models.DateTimeField(null=True)	
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac, related_name='customer_list', on_delete=models.SET_NULL, blank=True, null=True)	
    utc_offset_in_minutes = models.IntegerField(null=True)	
    zip = models.TextField(max_length=200)  

    def __str__(self):
        return str(self.code) 


class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    name = models.TextField(max_length=100)	
    #tac_id = models.IntegerField(null=True)
    tac = models.ForeignKey(Tac, related_name='organization_list', on_delete=models.SET_NULL, blank=True, null=True)
	  

    def __str__(self):
        return str(self.code)
    
    

class OrgCustomer(models.Model):
    org_customer_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #customer_id = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer, related_name='org_customer_list', on_delete=models.SET_NULL, blank=True, null=True)	
    email = models.TextField(max_length=100)	
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization, related_name='org_customer_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)

class Land(models.Model):
    land_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    description = models.TextField(max_length=200)	
    display_order = models.IntegerField(null=True)
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=50)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='land_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)

class Flavor(models.Model):
    flavor_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    description = models.TextField(max_length=200)	
    display_order = models.IntegerField(null=True)	
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=50)
	#pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='flavor_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)

class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #flavor_id = models.IntegerField(null=True)
    flavor = models.ForeignKey(Flavor, related_name='plant_list', on_delete=models.SET_NULL, blank=True, null=True)
    is_delete_allowed = models.BooleanField(null=True)
    is_edit_allowed = models.BooleanField(null=True)	
    #land_id = models.IntegerField(null=True)
    land = models.ForeignKey(Land, related_name='plant_list', on_delete=models.SET_NULL, blank=True, null=True)	
    other_flavor = models.TextField(max_length=50)
    some_big_int_val = models.BigIntegerField(null=True)
    some_bit_val = models.BooleanField(null=True)
    some_date_val = models.DateField(null=True)
    some_decimal_val = models.DecimalField(max_digits=18, decimal_places=6,null=True)
    some_email_address = models.TextField(max_length=50)
    some_float_val = models.FloatField(null=True)	
    some_int_val = models.IntegerField(null=True)	
    some_money_val = models.DecimalField(max_digits=19, decimal_places=4,null=True)
    some_n_var_char_val = models.TextField(max_length=50)
    some_phone_number = models.TextField(max_length=50)
    some_text_val = models.TextField(max_length=max)
    some_uniqueidentifier_val = models.UUIDField(null=True)
    some_utc_date_time_val = models.DateTimeField(null=True)
    some_var_char_val = models.TextField(max_length=50)  

    def __str__(self):
        return str(self.code)
    
class ErrorLog(models.Model):
    error_log_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    browser_code = models.UUIDField(null=True)
    context_code = models.UUIDField(null=True)
    created_utc_date_time = models.DateTimeField(null=True)
    description = models.TextField(max_length=max)
    is_client_side_error = models.BooleanField(null=True)
    is_resolved = models.BooleanField(null=True)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='error_log_list', on_delete=models.SET_NULL, blank=True, null=True)	
    url = models.TextField(max_length=500)  

    def __str__(self):
        return str(self.code)

class DateGreaterThanFilter(models.Model):
    date_greater_than_filter_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    day_count = models.IntegerField(null=True)
    description = models.TextField(max_length=500)	
    display_order = models.IntegerField(null=True)	
    is_active = models.BooleanField(null=True)
    lookup_enum_name = models.TextField(max_length=50)
    name = models.TextField(max_length=100)	
    #pac_id =  models.IntegerField(null=True)
    pac = models.ForeignKey(Pac, related_name='date_greater_than_filter_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)

class CustomerRole(models.Model):
    customer_role_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)	
    #customer_id = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer, related_name='customer_role_list', on_delete=models.SET_NULL, blank=True, null=True)	
    is_placeholder = models.BooleanField(null=True)
    placeholder = models.BooleanField(null=True)	
    #role_id = models.IntegerField(null=True)
    role = models.ForeignKey(Role, related_name='customer_role_list', on_delete=models.SET_NULL, blank=True, null=True)	  

    def __str__(self):
        return str(self.code)


class OrgApiKey(models.Model):
    org_api_key_id = models.AutoField(primary_key=True)
    code = models.UUIDField(default=uuid.uuid4)
    insert_utc_date_time =models.DateTimeField(default=timezone.now)
    last_udpate_utc_date_time =models.DateTimeField(default=timezone.now)
    insert_user_id = models.UUIDField(null=True)
    last_update_user_id = models.UUIDField(null=True)
    last_change_code = models.UUIDField(default=uuid.uuid4)
    api_key_value = models.TextField(max_length=4000)
    created_by = models.TextField(max_length=100)
    created_utc_date_time = models.DateTimeField(null=True)
    expiration_utc_date_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(null=True)
    is_temp_user_key = models.BooleanField(null=True)
    name = models.TextField(max_length=100)	
    #organization_id = models.IntegerField(null=True)
    organization = models.ForeignKey(Organization, related_name='org_api_key_list', on_delete=models.SET_NULL, blank=True, null=True)	
    #org_customer_id = models.IntegerField(null=True)
    org_customer = models.ForeignKey(OrgCustomer, related_name='org_api_key_list', on_delete=models.SET_NULL, blank=True, null=True)
	
	  

    def __str__(self):
        return str(self.code)