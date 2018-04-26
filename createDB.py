import sqlite3

conn = sqlite3.connect('medicine_db.db')
c = conn.cursor()
c.execute('''CREATE TABLE meds
             (uid integer, med_name text, expiration_data text, amount real,
              is_closed integer, city text, owner_mail test)''')
conn.commit()

conn.close()
