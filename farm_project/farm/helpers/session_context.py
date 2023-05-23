
import uuid
 
class SessionContext:
    user_name:str = "" 
    customer_code:uuid = uuid.UUID(int=0) 
    tac_code:uuid = uuid.UUID(int=0) 
    pac_code:uuid = uuid.UUID(int=0) 
    api_key_dict:dict = dict()
    session_code:uuid = uuid.UUID(int=0) 

    def __init__(self, api_key_dict:dict) -> None:
        self.api_key_dict = api_key_dict

    
    def check_context_code(self, 
                           context_code_name:str = "", 
                           context_code_value:uuid = uuid.UUID(int=0)) -> uuid:
        # if code dne or unknown then use the one in the api token
        if context_code_value == uuid.UUID(int=0) and self.api_key_dict[context_code_name] != None:
            return self.api_key_dict[context_code_name]
        
        return context_code_value



        