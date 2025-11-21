from login import register_user, log_in

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
            register_user()
        elif choice == '2':
            log_in()
            print('You log in seccesfuly !!!')

        elif choice == '3':
            print('Good Bye!!')
            break





import sqlite3


conn = sqlite3.connect('DATA/telligence_platform.db')

curr = conn.cursor()

sql = (""" CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL UNIQUE,
password_hash TEXT NOT NULL
       )""")

curr.execute(sql)

conn.commit()

conn.close()