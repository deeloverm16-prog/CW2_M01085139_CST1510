def add_user(conn, name, hash, role):
    curr = conn.cursor()
    sql = '''INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?) '''
    param =(name, hash, role) 
    curr.execute(sql, param)
    conn.commit()

def migrate_users(conn):
    with open(r'DATA/user.txt', 'r') as f:
        users = f.readlines()

    for user in users:
        name, hash, role = user.strip().split(',')
        add_user(conn, name, hash, role)


#read data from user
def get_all_users(conn):
    curr = conn.cursor()
    sql = '''SELECT * FROM users'''
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return(users)

#read just one user based on name
def get_user(conn, name):
    curr = conn.cursor()
    sql = '''SELECT * FROM users WHERE username = ?'''
    param = (name,)
    curr.execute(sql, param)
    user = curr.fetchone()
    conn.close()
    return(user)



def update_user(conn, old_name, new_name):
    curr = conn.cursor()
    sql= 'UPDATE users SET username = ? WHERE username = ?'
    param = (new_name,old_name)
    curr.execute(sql, param)
    conn.commit()


def delete_user(conn, user_name):
    curr = conn.cursor()
    sql= 'DELETE FROM users WHERE username = ?'
    param = (user_name,)
    curr.execute(sql, param)
    conn.commit()