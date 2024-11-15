import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task text NOT NULL, is_active BOOLEAN)")
con.commit()