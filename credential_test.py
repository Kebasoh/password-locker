import unittest
import pyperclip
from credential import Credential
from user import User

class TestUser(unittest.TestCase):
    
     def setUp(self):
         
         
          self.new_credential = ("Steve","Kebaso","kebasoh","steve254")
          
          
          
     def test_init(self):
          
        self.assertEqual(self.new_credential.account_name,"Steve")
        self.assertEqual(self.new_credential.password,"Kebaso")
       
               
         
     def test_save_credential(self):
       
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credential_list),1)
        
     def test_save_multiple_credential(self):
       
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","steve254") 
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
    
     def tearDown(self):
         
         Credential.credential_list = []

     def test_delete_credential(self):
        
         self.new_credential.save_credential()
         test_credential = Credential("Facebook","steve244") 
         test_credential.save_credential()

         self.new_credential.delete_credential()
         self.assertEqual(len(Credential.credential_list),1)
     def test_find_user_by_account_name(self):
         

         self.new_credential.save_credential()
         test_credential = Credential("Facebook","steve254")
         test_credential.save_credential()

         found_credential = Credential.find_by_account_name("Facebook")

         self.assertEqual(found_credential.account_name,test_credential.account_name)
     def test_credential_exists(self):
         

         self.new_credential.save_credential()
         test_credential = Credential("Facebook","steve254") 
         test_credential.save_credential()

         credential_exists = Credential.credential_exist("kebasoh")

         self.assertTrue(credential_exists)
     def test_display_all_credential(self):
       

         self.assertEqual(Credential.display_credential(),Credential.credential_list)
   
     def test_copy_password(self):
         

         self.new_credential.save_credential()
         Credential.copy_password("")

         self.assertEqual(self.new_credential.password,pyperclip.paste())

if __name__ ==  '__main__':
 unittest.main()
