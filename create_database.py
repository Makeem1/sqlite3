import sqlite3


def show_all():
    """Creating a connection customer db"""
    conn = sqlite3.connect(('customer.db'))

    """Creating cursor"""
    c = conn.cursor()

    """Showing all the table data"""    
    c.execute("SELECT rowid, * FROM customers")

    """Committing into the database"""
    conn.commit()

    """Creating a query """
    items = c.fetchall()

    for item in items:
        print(item)
    """Closing the database """
    conn.close()


def insert_one(firstname, lastname, email):
    """Creating a connection customer db"""
    conn = sqlite3.connect(('customer.db'))

    """Creating cursor"""
    c = conn.cursor()

    """Showing all the table data"""    
    c.execute("INSERT INTO customers VALUES (?,?,?)", (firstname, lastname, email))
    
    """Committing into the database"""
    conn.commit()

    """Closing the database """
    conn.close()


def insert_many(listdata):
    """Creating a connection customer db"""
    conn = sqlite3.connect(('customer.db'))

    """Creating cursor"""
    c = conn.cursor()

    """Showing all the table data"""    
    c.executemany("INSERT INTO customers VALUES (?,?,?)", listdata)
    
    """Committing into the database"""
    conn.commit()

    """Closing the database """
    conn.close()


def update_table_lastname(lastname = None, rowid = None):
    """Creating a connection customer db"""
    conn = sqlite3.connect(('customer.db'))

    """Creating cursor"""
    c = conn.cursor()

    if lastname and rowid :
        """updating a the table data"""    
        c.execute("UPDATE customers SET lastname = (?) WHERE rowid = (?)", (lastname, rowid) )
    else:
        """updating a the table data""" 
        print("\n")
        print("You need to specify the lastname and id of the data before update can be made ")
        print('\n')
        
    """Committing into the database"""
    conn.commit()

    """ Closing the database """
    conn.close()


def update_table_firstname(firstname = None, rowid = None):
    """Creating a connection customer db"""
    conn = sqlite3.connect(('customer.db'))

    """Creating cursor"""
    c = conn.cursor()

    if firstname and rowid :
        """updating a the table data"""    
        c.execute("UPDATE customers SET firstname = (?) WHERE rowid = (?)", (firstname, rowid) )
    else:
        """updating a the table data""" 
        print("\n")
        print("You need to specify the firstname and id of the data before update can be made ")
        print('\n')
        
    """Committing into the database"""
    conn.commit()

    """ Closing the database """
    conn.close()

def update_table_email(email = None, rowid = None):
    """Creating a connection customer db"""
    conn = sqlite3.connect(('customer.db'))

    """Creating cursor"""
    c = conn.cursor()

    if email and rowid :
        """updating a the table data"""    
        c.execute("UPDATE customers SET email = (?) WHERE rowid = (?)", (email, rowid) )
    else:
        """updating a the table data""" 
        print("\n")
        print("You need to specify the email and id of the data before update can be made ")
        print('\n')
        
    """Committing into the database"""
    conn.commit()

    """ Closing the database """
    conn.close()


def delete_data(id):
    """Creating a connection customer db"""
    conn = sqlite3.connect(('customer.db'))

    """Creating cursor"""
    c = conn.cursor()

    if id:
        c.execute('DELETE from customers WHERE rowid = (?) ', id)
    else:
        print("You need to input the id of the data you want to delete from the table ")

    """Committing into the database"""
    conn.commit()

    """ Closing the database """
    conn.close()



def order_data(lastname):
    """Creating a database """
    conn = sqlite3.connect("customer.db")

    """Creating a database """
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%mk.com' ORDER BY lastname" )
     
    """Committing into the database"""
    conn.commit()

    result = c.fetchall()
    for item in result:
        print(item )
    """ Closing the database """
    conn.close()



# many_customers = [
#     ('John', 'Doe', 'hohndoe@gmail.com'),
#     ('Ron', 'Doe', 'Ron@gmail.com'),
#     ('John', 'Lyric', 'lyric@gmail.com'),
# ]

# def insert_one(firstname, lastname, email):
#     """ creating a database """
#     # conn = sqlite3.connect('customer.db')
#     """ creating cursor """
#     c = conn.cursor()

#     '''Inserting date into table created'''
#     result = c.execute("INSERT INTO customers VALUES (?,?,?)", (firstname, lastname, email)) 
#     conn.commit()
#     """Commiting the data into table"""
#     print(c.fetchone())
#     # conn.commit()
#     """Closing the table"""
#     conn.close()

# insert_one("ola", 'kola', 'ola@gmail.com')


# '''Inserting many data into table created'''
# # c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# '''
#     Querying data from the table created and also query the table. fetchone, fetchall, and fetchmany is use to fetch data from the table. Using the WHERE and LIKE clause to fetch a particular data from the table. 

#     Note : All comparison operator can be used with WHERE clause
    
# '''

# # c.execute("SELECT rowid, * FROM customers WHERE firstname = 'Ola' ")
# c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%.com' ")
# # c.fetchone()  
# # c.fetchmany(3) 

# c.execute("UPDATE customers SET firstname = 'john' WHERE rowid = 22 ")
# c.execute("UPDATE customers SET firstname = 'Ola' WHERE rowid = 1 ")
# c.execute("SELECT rowid, * FROM customers WHERE firstname = 'john' ")


# """Delting data from table"""
# # c.execute("DELETE from customers WHERE  rowid = 1 ")

# """Ordering table"""
# # c.execute("SELECT rowid, * FROM customers ORDER BY firstname = 'john' DESC ")

# """Using conditional statement OR and AND for querying table"""
# # c.execute('SELECT * FROM customers WHERE lastname LIKE "%oe" OR rowid = 2 ')

# """Limiting a search result """
# c.execute("SELECT rowid, * FROM customers WHERE lastname = 'Doe' ORDER BY rowid = 2 LIMIT 5")

# """Deleting the entire table"""
# c.execute('DROP TABLE customers')
# print("Table deleted")


# conn.commit()

# items = c.fetchall() 


# for item in items:
#     print(item)
# print("command executed successfully...")

# """Commiting the data into table"""
# conn.commit()

# """Closing the table"""
# conn.close()



