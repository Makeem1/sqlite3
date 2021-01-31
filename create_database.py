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

'''Inserting date into table created'''
c.execute("INSERT INTO customers VALUES ('Ola', 'Akeem', 'Ola@example.com')")

"""Commiting the data into table"""
conn.commit()

"""Closing the table"""
conn.close()



