import pyperclip
class User:
   
    user_list = []

    def __init__(self,first_name,last_name,username,password):

    

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        
    user_list = []
    def save_user(self):

       

        User.user_list.append(self)
    def delete_user(self):
    
       

        User.user_list.remove(self)
    @classmethod
    def find_by_username(cls,username):
       

        for user in cls.user_list:
            if user.username == username:
                return username
    @classmethod
    def user_exist(cls,username):
       
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False
    @classmethod
    def display_username(cls):
       
        return cls.user_list
    
    @classmethod
    def copy_password(cls,password):
        user_found = User.find_by_password(username)
        pyperclip.copy(user_found.password)
    