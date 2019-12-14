#!/usr/bin/env python3.6
from user import User

def __init__(account_name,user_name,password,email):
   
    new_user = User(account_name,user_name,password,email)
    return new_user
def save_user(user):
   
    user.save_user()