import pyperclip
class User:
    
    user_list = []
    
    def __init__(self,account_name,user_name,password,email):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email
        
        
    user_list = [] 
    def save_user(self):

      

        User.user_list.append(self)
        
    def delete_user(self):
    
       User.user_list.remove(self)
       
    @classmethod
    def find_by_user(cls,user_name):
       

        for user in cls.user_list:
            if user.user_name == user_name:
                return user
    @classmethod
    def user_exist(cls,user_name):
       
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False
    
    @classmethod
    def display_user(cls):
       
        return cls.user_list
   
    @classmethod
    def copy_password(cls,user_name):
        user_found = User.find_by_user(user_name)
        pyperclip.copy(user_found.password)