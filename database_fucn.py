import create_database 

# create_database.insert_one('akeem', 'ola', 'ola@dd.com')

create_database.update_table_lastname('john', 1)
create_database.update_table_firstname("Moshood", 5)
create_database.update_table_email("last@last.com", 5)

listdata = [
    ('stiff', 'john', "stifJohn@mk.com"),
    ('hosh', 'john', "hushjohn@mk.com"),
    ('lolly', 'pop', "lollypop@mk.com"),

]
create_database.insert_many(listdata)

create_database.show_all()



