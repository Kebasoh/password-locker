import unittest
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

if __name__ ==  '__main__':
 unittest.main()