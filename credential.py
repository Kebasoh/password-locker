import pyperclip
class Credential:
   
    credential_list = []

    def __init__(self,accout_name,password,):

    

        self.account_name = accout_name
        self.password = password
       
        
    credential_list = []
    def save_credential(self):

       

        Credential.user_list.append(self)
    def delete_credential(self):
    
       

        Credential.credential_list.remove(self)
    @classmethod
    def find_by_account_name(cls,account_name):
       

        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return account_name
    @classmethod
    def credential_exist(cls,account_name):
       
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                    return True

        return False
    @classmethod
    def display_account_name(cls):
       
        return cls.credential_list
    
    @classmethod
    def copy_password(cls,password):
        credential_found = Credential.find_by_password(password)
        pyperclip.copy(credential_found.password)
    