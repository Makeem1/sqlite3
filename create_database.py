import sqlite3


""" Creating database """
conn = sqlite3.connect('customer.db')

# creating cursor
c = conn.cursor()

''' Creating table ''' 
# c.execute("""CREATE TABLE customers(
#     firstname text,
#     lastname text,
#     email text
# )""")

"""Adding many data into the customers table at once, a list of turple is created """
many_customers = [
    ('John', 'Doe', 'hohndoe@gmail.com'),
    ('Ron', 'Doe', 'Ron@gmail.com'),
    ('John', 'Lyric', 'lyric@gmail.com'),
]

'''Inserting date into table created'''
# c.execute("INSERT INTO customers VALUES ('Ola', 'Akeem', 'Ola@example.com')") 

'''Inserting many data into table created'''
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

'''Querying data from the table created'''
c.execute("SELECT rowid, * FROM customers")
# print(c.fetchone())   #This help to query the first data in the table 
# print(c.fetchmany(3)) #This help to query specified data from the table
items = c.fetchall() #This help to query all data from the table

print("NAME " + "\t\t" +  "EMAIL" )
for item in items:
    print(f"'{item[0]}'  {item[1]}  {item[2]}")
print("command executed successfully...")

"""Commiting the data into table"""
conn.commit()

"""Closing the table"""
conn.close()



