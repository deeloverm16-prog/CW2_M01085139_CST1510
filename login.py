import bcrypt
import sqlite3

#hashed using bcrypt 
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
    hash = hash_password(user_password)
    add_user(conn, user_name ,hash)



#user login
def log_in():
    user_name = input('Enter user name: ')
    user_password = input('Enter your password:')
    role = input('Enter your role: ')
    with open('DATA/user.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            name,hash,stored_role = line.strip().split(',')
            if name == user_name and role == stored_role:
                return validate_password(user_password, hash)
    return False


