import sqlite3

conn = sqlite3.connect('medicine_db.db')
c = conn.cursor()
# c.execute('''CREATE TABLE meds
#              (uid integer, med_name text, expiration_data text, amount real,
#               is_closed integer, city text, owner_mail test)''')

c.execute("INSERT INTO meds VALUES (1, 'Malarone', '2018-05-01', 10, 0, 'Haifa', 'shahar.aizenbud@gmail.com')")


conn.commit()

conn.close()
