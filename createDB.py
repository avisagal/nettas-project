import sqlite3

conn = sqlite3.connect('medicine_db.db')
c = conn.cursor()
# c.execute('''CREATE TABLE meds
#              (uid integer, med_name text, expiration_data text, amount real,
#               is_closed integer, city text, owner_mail test)''')

#c.execute("INSERT INTO meds VALUES (1, 'Malarone', '2018-05-01', 10, 0, 'Haifa', 'shahar.aizenbud@gmail.com')")

values = [(2, 'Acamol', '2018-06-22', 20, 1, 'Jerusalem', 'avisagal41@gmail.com'),
          (3, 'Advil', '2019-01-01', 15, 0, 'Jerusalem', 'netta.barak@gmail.com')]
c.executemany("INSERT INTO meds VALUES (?,?,?,?,?,?,?)", values)



conn.commit()

conn.close()
