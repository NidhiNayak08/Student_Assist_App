import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("create table userlogin (username text, password text)")

login_list = [
    ("Tim","aa"),
    ("Tina","aa"),
    ("Bob","aa"),
    ("Katy","aa"),
    ("Aastha","aa"),
    ("Pranathi","aa"),
    ("Nidhi","aa"),
    ("Bhavishka","aa")
]

c.executemany("insert into userlogin values (?,?)",login_list)
c.execute('select * from userlogin')
rows = c.fetchall()

#print table values
table = PrettyTable(['Username','Password'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)

conn.commit()
conn.close()
