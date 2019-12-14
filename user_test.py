import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    
     def setUp(self):
         
         
          self.new_user = User("Steve","Kebasoh","steve254","ongatikebaso@gmail.com")
          
          
          
     def test_init(self):
               
               
          self.assertEqual(self.new_user.account_name,"Steve")
          self.assertEqual(self.new_user.user_name,"Kebasoh")
          self.assertEqual(self.new_user.password,"steve254")
          self.assertEqual(self.new_user.email,"ongatikebaso@gmail.com")
   
     def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
        
     def test_save_multiple_user(self):
           
            self.new_user.save_user()
            test_user = User("Test","user","steve254","test@user.com")
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
          
     def tearDown(self):
           
            User.user_list = []

     def test_save_multiple_user(self):
           
            self.new_user.save_user()
            test_user = User("Test","user","steve254","test@user.com") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
            
     def test_delete_user(self):
               
            self.new_user.save_user()
            test_user = User("Test","user","steve254","test@user.com") 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)
            
            
     def test_user_exists(self):
           

        self.new_user.save_user()
        test_user = User("Test","user","steve254","test@user.com")
        test_user.save_user()

        user_exists = User.user_exist("steve254")
        self.assertTrue(user_exists)
        
     def test_display_all_user(self):
           

        self.assertEqual(User.display_user(),User.user_list)



if __name__ ==  '__main__':
 unittest.main()