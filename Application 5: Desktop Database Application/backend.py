""" 
Program to design a Desktop Database Appliction
in Python using tkinter and sqlite3 
for maintaining a Bookstore database and 
add,search,delete,update and view book information
	
	by Aniruddha
	
~~~~~~~~~~~BackEnd Part~~~~~~~~~~~~
"""

import sqlite3

def connect():
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Book(Id INTEGER PRIMARY KEY,Title TEXT,Author TEXT,Year INTEGER,ISBN INTEGER)")
	conn.commit()
	conn.close()

def insert(Title,Author,Year,ISBN):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO Book VALUES(NULL,?,?,?,?)",(Title,Author,Year,ISBN))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM Book")
	rows = cur.fetchall()
	conn.close()
	return rows
		
def search(Title="",Author="",Year="",ISBN=""):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM Book WHERE Title = ? OR Author = ? OR Year = ? OR ISBN = ?",(Title,Author,Year,ISBN))
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM Book WHERE Id = ?",(id,))
	conn.commit()
	conn.close()

def update(id,Title,Author,Year,ISBN):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("UPDATE Book SET Title = ?,Author = ?,Year = ?,ISBN = ? WHERE Id =?",(Title,Author,Year,ISBN,id))
	conn.commit()
	conn.close()

connect()
#insert("Like a Hole in The Head","James Hadley Chase",1970,9781842321126)
#view()	
#search(Author = "ani")
#delete(2)
#update(4,"moon","aniruddha",2018,123456789)
view()
