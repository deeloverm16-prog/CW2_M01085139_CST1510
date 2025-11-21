import bcrypt

def hash_password(password):
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(binary_password, salt)
    return hashed.decode('utf-8')

def validate_password(password, hash):
    password_bytes = password.encode('utf-8')
    hashed_bytes = hash.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user():
    user_name = input('Enter your username: ')
    user_password = input('Enter your password: ')
    hashed_password = hash_password(user_password)
    with open('user.txt', 'a') as f:
        f.write(f'{user_name},{hashed_password}\n')
    print('User registered successfully!!!')

def log_in():
    user_name = input('Enter user name: ')
    user_password = input('Enter your password:')
    with open('user.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            name,hash = line.strip().split(',')
            if name == user_name:
                return validate_password(user_password, hash)
    return False
