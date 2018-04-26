import sqlite3

conn = sqlite3.connect('medicine_db.db')
c = conn.cursor()
# c.execute('''CREATE TABLE meds
#              (uid integer, med_name text, expiration_data text, amount real,
#               is_closed integer, city text, owner_mail test)''')

#c.execute("INSERT INTO meds VALUES (1, 'Malarone', '2018-05-01', 10, 0, 'Haifa', 'shahar.aizenbud@gmail.com')")

# values = [(2, 'Acamol', '2018-06-22', 20, 1, 'Jerusalem', 'avisagal41@gmail.com'),
#           (3, 'Advil', '2019-01-01', 15, 0, 'Jerusalem', 'netta.barak@gmail.com')]
# c.executemany("INSERT INTO meds VALUES (?,?,?,?,?,?,?)", values)

# c.execute('''CREATE TABLE meds_data
#              (med_name text, picture text)''')

values = [('Malarone', 'https://www.doctorfox.co.uk/imgs-products/zoom/malarone-pills.jpg'),
          ('Acamol', 'http://www.pilula.co.il/~pilula5/images/stories/virtuemart/product/acamol%20caps.jpg'),
          ('Advil', 'https://images-na.ssl-images-amazon.com/images/I/917DL6AA0PL._SY355_.jpg'),
          ('Meliane', 'http://www.drug.co.il/ps/109-12-29094-00.jpg'),
          ]
c.executemany("INSERT INTO meds_data VALUES (?,?)", values)




conn.commit()

conn.close()
