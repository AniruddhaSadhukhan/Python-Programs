""" 
Program to design a Desktop Database Appliction
in Python using tkinter and sqlite3 by OOP approach
for maintaining a Bookstore database and 
add,search,delete,update and view book information
	
	by Aniruddha
	
~~~~~~~~~~~BackEnd Part~~~~~~~~~~~~
"""

import sqlite3

class Database:
	def __init__(self,db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS Book(Id INTEGER PRIMARY KEY,Title TEXT,Author TEXT,Year INTEGER,ISBN INTEGER)")
		self.conn.commit()

	def insert(self,Title,Author,Year,ISBN):
		self.cur.execute("INSERT INTO Book VALUES(NULL,?,?,?,?)",(Title,Author,Year,ISBN))
		self.conn.commit()

	def view(self):
		self.cur.execute("SELECT * FROM Book")
		rows = self.cur.fetchall()
		return rows
		
	def search(self,Title="",Author="",Year="",ISBN=""):
		self.cur.execute("SELECT * FROM Book WHERE Title = ? OR Author = ? OR Year = ? OR ISBN = ?",(Title,Author,Year,ISBN))
		rows = self.cur.fetchall()
		return rows

	def delete(self,id):
		self.cur.execute("DELETE FROM Book WHERE Id = ?",(id,))
		self.conn.commit()

	def update(self,id,Title,Author,Year,ISBN):
		self.cur.execute("UPDATE Book SET Title = ?,Author = ?,Year = ?,ISBN = ? WHERE Id =?",(Title,Author,Year,ISBN,id))
		self.conn.commit()
		
	def __del__(self):
		self.conn.close()

