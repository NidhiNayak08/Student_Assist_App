import sqlite3
from prettytable import PrettyTable

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('tododatabase.db')
# Create a cursor object to execute SQL commands
cur = conn.cursor()




# Create the first table
cur.execute('''CREATE TABLE Tim
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Tim (task, status) VALUES (?, ?)", ('math tutorial', 'incomplete'))
cur.execute("INSERT INTO Tim (task, status) VALUES (?, ?)", ('coa lab', 'complete'))

cur.execute('select * from Tim')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)





# Create the second table
cur.execute('''CREATE TABLE Tina
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Tina (task, status) VALUES (?, ?)", ('coa assignment', 'incomplete'))
cur.execute("INSERT INTO Tina (task, status) VALUES (?, ?)", ('cn lab', 'complete'))

cur.execute('select * from Tina')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)





# Create the third table
cur.execute('''CREATE TABLE Bob
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Bob (task, status) VALUES (?, ?)", ('python tutorial', 'incomplete'))
cur.execute("INSERT INTO Bob (task, status) VALUES (?, ?)", ('os lab', 'complete'))

cur.execute('select * from Bob')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)





# Create the fourth table
cur.execute('''CREATE TABLE Katy
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Katy (task, status) VALUES (?, ?)", ('os viva', 'incomplete'))
cur.execute("INSERT INTO Katy (task, status) VALUES (?, ?)", ('python lab', 'complete'))

cur.execute('select * from Katy')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)





# Create the fifth table
cur.execute('''CREATE TABLE Aastha
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Aastha (task, status) VALUES (?, ?)", ('math project', 'incomplete'))
cur.execute("INSERT INTO Aastha (task, status) VALUES (?, ?)", ('os lab', 'complete'))

cur.execute('select * from Aastha')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)




# Create the sixth table
cur.execute('''CREATE TABLE Pranathi
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Pranathi (task, status) VALUES (?, ?)", ('python project', 'incomplete'))
cur.execute("INSERT INTO Pranathi (task, status) VALUES (?, ?)", ('cn lab', 'complete'))

cur.execute('select * from Pranathi')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)




# Create the seventh table
cur.execute('''CREATE TABLE Nidhi
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Nidhi (task, status) VALUES (?, ?)", ('at assignment', 'incomplete'))
cur.execute("INSERT INTO Nidhi (task, status) VALUES (?, ?)", ('os lab', 'complete'))

cur.execute('select * from Nidhi')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)




# Create the eighth table
cur.execute('''CREATE TABLE Bhavishka
               (task TEXT, status TEXT)''')

# Insert values into the table
cur.execute("INSERT INTO Bhavishka (task, status) VALUES (?, ?)", ('cn assignment', 'incomplete'))
cur.execute("INSERT INTO Bhavishka (task, status) VALUES (?, ?)", ('python project', 'complete'))

cur.execute('select * from Bhavishka')
rows = cur.fetchall()

#print table values
table = PrettyTable(['Task','Status'])
#add rows to the table
for row in rows:
    table.add_row(row)

print(table)




# Commit the changes and close the connection
conn.commit()
conn.close()
