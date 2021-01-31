import sqlite3


""" Creating database """
conn = sqlite3.connect('customer.db')
print(conn)
# creating cursor
c = conn.cursor()
print(c)
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

'''
    Querying data from the table created and also query the table. fetchone, fetchall, and fetchmany is use to fetch data from the table. Using the WHERE and LIKE clause to fetch a particular data from the table. 

    Note : All comparison operator can be used with WHERE clause
    
'''

# c.execute("SELECT rowid, * FROM customers WHERE firstname = 'Ola' ")
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%.com' ")
# c.fetchone()  
# c.fetchmany(3) 

c.execute("UPDATE customers SET firstname = 'john' WHERE rowid = 22 ")
c.execute("UPDATE customers SET firstname = 'Ola' WHERE rowid = 1 ")
c.execute("SELECT rowid, * FROM customers WHERE firstname = 'john' ")


"""Delting data from table"""
# c.execute("DELETE from customers WHERE  rowid = 1 ")

"""Ordering table"""
# c.execute("SELECT rowid, * FROM customers ORDER BY firstname = 'john' DESC ")

"""Using conditional statement OR and AND for querying table"""
# c.execute('SELECT * FROM customers WHERE lastname LIKE "%oe" OR rowid = 2 ')

"""Limiting a search result """
c.execute("SELECT rowid, * FROM customers WHERE lastname = 'Doe' ORDER BY rowid = 2 LIMIT 5")

"""Deleting the entire table"""
c.execute('DROP TABLE customers')
print("Table deleted")


conn.commit()

items = c.fetchall() 


for item in items:
    print(item)
print("command executed successfully...")

"""Commiting the data into table"""
conn.commit()

"""Closing the table"""
conn.close()



