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