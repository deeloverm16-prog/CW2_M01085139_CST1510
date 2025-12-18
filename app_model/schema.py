#Create db table for the users
def create_user_table(conn):
    curr = conn.cursor()
    sql = '''CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user');
            '''
    curr.execute(sql)
    conn.commit()
