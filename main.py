import bcrypt
import sqlite3
import pandas as pd


from app_model.db import conn
from app_model.users import add_user, get_user


def hash_password(password):
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(binary_password, salt)
    return hashed.decode('utf-8')

#validating hash as psw
def validate_password(password, hash):
    password_bytes = password.encode('utf-8')
    hashed_bytes = hash.encode('utf-8')
    valid = bcrypt.checkpw(password_bytes, hashed_bytes)
    return valid

#user registration
def register_user(conn):
    user_name = input('Enter your username: ')
    user_password = input('Enter your password: ')
    role = input('Enter your role: ')
    psw_hash = hash_password(user_password)
    add_user(conn,user_name ,psw_hash ,role)



#user login
def log_in(conn):
    user_name = input('Enter user name: ')
    user_password = input('Enter your password: ')
    id, name, user_hash, role = get_user(conn, user_name)
    
    print(f'Welcome {name} !!')
    if user_name == name :
            return validate_password(user_password, user_hash)
    return False

def menu():
    print('Welcome to my system')
    print('Choose from following options')
    print('1. Register')
    print('2. Log in')
    print('3. To Exit ')

def main():
    while True:
        menu()
        choice = input(' > ')
        if choice == '1':
            register_user(conn)
        elif choice == '2':
            if log_in(conn):
                print('You logged in successfuly !!!\n')
            else:
                print("Login failed. Invalid username or password.")
        elif choice == '3':
            print('Good Bye!!')
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ ==  '__main__':
    main()

















conn = sqlite3.connect('DATA/project_data.db')
