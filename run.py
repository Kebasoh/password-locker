#!/usr/bin/env python3.6
from user import User

def __init__(account_name,user_name,password,email):
   
    new_user = User(account_name,user_name,password,email)
    return new_user
def save_user(user):
   
    user.save_user()
def del_user(user):
     
    user.delete_user()
def find_user(user_name):
    
    return User.find_by_user_name(user_name)

def check_existing_user(user_name):
    
    return User.user_exist(user_name)
def display_user():
  
    return User.display_user()