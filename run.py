#!/usr/bin/env python3.6
import pyperclip
from user import User
from Crypto.Util import number
def create_user(fname,lname,username,password):
   
    new_user = User(fname,lname,username,password)
    return new_user
def save_user(user):
    
    user.save_user()
def del_user(user):
   
    user.delete_user()
def find_user(username):
  
    return User.find_by_username(username)
def check_existing_user(username):
    
    return User.user_exist(username)
def display_user():
    
    return User.display_username()
def copy_password(username):
    
    return User.copy_password(username)
def main():
    print('Hello! Welcome to your user list. What is your name?')
    user_name = input()
    print(f"Hello {user_name}. What would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: cu - create a new user, du - display user, del - delete user, cp - copy password, fp - find a password, ex - exit the user list ")
        short_code = input().lower().strip()
        if short_code == 'cu':
            print('New User')
            print("-"*30)
            print('First name ...')
            f_name = input()
            print("Last name ...")
            l_name = input()
            print("username ...")
            user_name = input()
            print("password ...")
            password = input()
            save_user(create_user(f_name,l_name,user_name,password)) 
            print('\n')
            print(f"New User {f_name} {l_name} created")
            print('\n')
        elif short_code == 'du':
            if display_user():
                print('Here is a list of all your users')
                print('\n')
                for user in display_user():
                    print(f'{user.first_name} {user.last_name} .....{User.password}')
                    print('\n')
            else:
                print('\n')
                print("You don't seem to have any users saved yet")
                print('\n')
        elif short_code == 'fp':
            print('Enter the username you want to search for')
            search_username = input()
            if check_existing_user(search_username):
                search_user = find_user(search_username)
                print(f"{search_user.first_name} {search_user.last_name}")
                print("-"*30)
                print(f"username.......{search_user.username}")
                print(f"password.......{search_user.password}")
            else :
                print('That user does not exist')
        elif short_code == 'del':
            print('Enter the username of the user to delete')
            search_username = input()
            if check_existing_user(search_username):
                search_user = find_user(search_username)
                del_user(search_user)
            else :
                print('That user does not exist')
        elif short_code == 'cp':
            print('Enter the username of the user whose password to copy')
            search_username = input()
            if check_existing_user(search_username):
                copy_password(search_username)
                print('password  has been copied')
            else:
                print('Please enter a valid password')
        elif short_code == 'ex':
            print('Bye..................')
            break
        else:
            print('I really didn\'t get that. Please use the short codes')
if __name__ == '__main__':
   main()