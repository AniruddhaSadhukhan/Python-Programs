""" 
Program to interface a SQL database in python
	by Aniruddha

***
Standard Procedure of Interacting with database:
1. Connect to database
2. Create a cursor object
3. Write an SQL query
4. Commit the changes
5. Close the connection

""" 
import sqlite3

def create_table():
	conn = sqlite3.connect("sql_database.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Store (Item TEXT,Quantity INTEGER,Price REAL)")
	conn.commit()
	conn.close()

def insert(item,qty,price):
	conn = sqlite3.connect("sql_database.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO Store VALUES(?,?,?)",(item,qty,price))
	conn.commit()
	conn.close()

def delete(item):
	conn = sqlite3.connect("sql_database.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM Store WHERE Item=?",(item,))
	conn.commit()
	conn.close()

def update(item,qty,price):
	conn = sqlite3.connect("sql_database.db")
	cur = conn.cursor()
	cur.execute("UPDATE Store SET Quantity=?,Price=? WHERE Item=?",(qty,price,item))
	conn.commit()
	conn.close()
	
def display():
	conn = sqlite3.connect("sql_database.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM Store")
	rows=cur.fetchall()
	conn.close()
	for r in rows:
		print(r)


create_table()
print("\nAfter Inserting:\n")
insert("A B",10,5.5)
insert("C D",8,10)
insert("E F",5,15.5)
display()
print("\nAfter Updating A B:\n")
update("A B",15,6)
display()
print("\nAfter Deleting C D:\n")
delete("C D")
display()


#***
#	After Inserting:

#	('A B', 10, 5.5)
#	('C D', 8, 10.0)
#	('E F', 5, 15.5)

#	After Updating A B:

#	('A B', 15, 6.0)
#	('C D', 8, 10.0)
#	('E F', 5, 15.5)

#	After Deleting C D:

#	('A B', 15, 6.0)
#	('E F', 5, 15.5)
#***
