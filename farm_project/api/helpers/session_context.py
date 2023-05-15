
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



        