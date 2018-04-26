import sqlite3

conn = sqlite3.connect('medicine_db.db')
c = conn.cursor()


conn.close()
