""" 
Program to design a Desktop Database Appliction
in Python using tkinter and sqlite3 by OOP approach
for maintaining a Bookstore database and 
add,search,delete,update and view book information
	
	by Aniruddha
	
-->For making a standalone application :
	1)Install pyinstaller(pip install pyinstaller)
	2)Run: pyinstaller filename.py
	
~~~~~~~~~~~FrontEnd Part~~~~~~~~~~~~
"""
 
#~~~~~~~~Building GUI~~~~~~~~#

from backend import Database
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

database = Database("books.db")

class Window(object):
	
	def __init__(self,window):
		
		self.win = window
		self.win.title("BookStore Management Software by Aniruddha")


		#Creating the labels
		lTitle = Label(self.win,text = "Title")
		lTitle.grid(row =1,column=1)
		
		lYear = Label(self.win,text = "Year")
		lYear.grid(row =2,column=1)

		lAuthor = Label(self.win,text = "Author")
		lAuthor.grid(row =1,column=5)

		lISBN = Label(self.win,text = "ISBN")
		lISBN.grid(row =2,column=5)



		#Creating the entryboxes
		self.eTitle = Entry(self.win)
		self.eTitle.grid(row = 1, column = 2,columnspan = 3)

		self.eYear = Entry(self.win)
		self.eYear.grid(row = 2, column = 2,columnspan = 3)

		self.eAuthor = Entry(self.win)
		self.eAuthor.grid(row = 1, column = 6,columnspan = 2)

		self.eISBN = Entry(self.win)
		self.eISBN.grid(row = 2, column = 6,columnspan = 2)



		#Creating the box listing the books(ttk.Treeview)
		listbox_headers = ["ID","Title","Author","Year",'ISBN']
		listbox_width = [24,150,110,40,111]
		self.listbox = ttk.Treeview(self.win,height=6,columns=listbox_headers ,show = "headings")
		for col,wid in zip(listbox_headers,listbox_width):
			self.listbox.heading(col,text=col)
			self.listbox.column(col,width=wid,stretch=0)
		self.listbox.grid(row =3,column=1,columnspan = 5,rowspan =6,sticky = "ns")


		#Creating the scrollbars for the list of books(ttk.Treeview)
		yscroll = Scrollbar(self.win)
		yscroll.grid(row =3,column=6,rowspan =6,sticky="ns")

		xscroll = Scrollbar(self.win,orient = HORIZONTAL)
		xscroll.grid(row =9,column=1,columnspan = 5,sticky="ew")


		#configure scrollbars and list for synchronisation
		self.listbox.configure(yscrollcommand = yscroll.set)
		yscroll.configure(command = self.listbox.yview)

		self.listbox.configure(xscrollcommand = xscroll.set)
		xscroll.configure(command = self.listbox.xview)


		#binding event to the list
		self.listbox.bind('<<TreeviewSelect>>',self.get_selected_row)


		#creating the buttons for different functions
		bView = Button(self.win,text = "View All",width=12,command = self.view_command)
		bView.grid(row =3,column=7)

		bSearch = Button(self.win,text = "Search",width=12,command = self.search_command)
		bSearch.grid(row =4,column=7)

		bAdd = Button(self.win,text = "Add Entry",width=12,command = self.insert_command)
		bAdd.grid(row =5,column=7)

		bUpdate = Button(self.win,text = "Update Selected",width=12,command = self.update_command)
		bUpdate.grid(row =6,column=7)

		bDelete = Button(self.win,text = "Delete Selected",width=12,command = self.delete_command)
		bDelete.grid(row =7,column=7)

		bClose = Button(self.win,text = "Close",width=12,command = win.destroy)
		bClose.grid(row =8,column=7)


		#configuring the rows and columns for extra spacing
		self.win.grid_rowconfigure(0,minsize = 20)
		self.win.grid_rowconfigure(9,minsize = 1)
		self.win.grid_rowconfigure(10,minsize = 20)
		for r in range(9):
			self.win.grid_rowconfigure(r,pad = 10)
		self.win.grid_columnconfigure(0,minsize = 30)
		self.win.grid_columnconfigure(8,minsize = 30)

		self.win.grid_columnconfigure(6,weight = 1)
		self.win.grid_columnconfigure(7,weight = 100)

	
	#defines what happens when a entry is selected
	def get_selected_row(self,event):
		global selection_id 
		selection_tuple = self.listbox.item(self.listbox.selection()[0],'values')
		selection_id = selection_tuple[0]
		entryboxes = [self.eTitle,self.eAuthor,self.eYear,self.eISBN]
		for e,data in zip(entryboxes,selection_tuple[1:]):
			e.delete(0,END)
			e.insert(0,data)


	#wrapper function for view
	def view_command(self):
		for row in self.listbox.get_children():
			self.listbox.delete(row)
		for row in database.view():
			self.listbox.insert('','end',values=row)


	#wrapper function for search
	def search_command(self):
		for row in self.listbox.get_children():
			self.listbox.delete(row)
		for row in database.search(self.eTitle.get(),self.eAuthor.get(),self.eYear.get(),self.eISBN.get()):
			self.listbox.insert('','end',values=row)


	#wrapper function for inserting
	def insert_command(self):
		if self.eTitle.get()=="" or self.eAuthor.get()=="" or self.eYear.get()=="" or self.eISBN.get()=="": 
			messagebox.showinfo("Alert", "Enter all the fields")
		else:database.insert(self.eTitle.get(),self.eAuthor.get(),self.eYear.get(),self.eISBN.get())
		for row in self.listbox.get_children():
			self.listbox.delete(row)
		self.listbox.insert('','end',values=("",self.eTitle.get(),self.eAuthor.get(),self.eYear.get(),self.eISBN.get()))


	#wrapper function for deleting
	def delete_command(self):
		try:
			database.delete(selection_id)
			self.listbox.delete(self.listbox.selection())
			self.eTitle.delete(0,END)
			self.eAuthor.delete(0,END)
			self.eYear.delete(0,END)
			self.eISBN.delete(0,END)
		except NameError:
			messagebox.showinfo("Alert", "An entry is not selected to delete")


	#wrapper function for updating
	def update_command(self):
		try:
			if self.eTitle.get()=="" or self.eAuthor.get()=="" or self.eYear.get()=="" or self.eISBN.get()=="": 
				messagebox.showinfo("Alert", "Enter all the fields")
			else:
				database.update(selection_id,self.eTitle.get(),self.eAuthor.get(),self.eYear.get(),self.eISBN.get())
				index = self.listbox.index(self.listbox.selection())
				self.listbox.delete(self.listbox.selection())
				self.listbox.insert('',index,values=(selection_id,self.eTitle.get(),self.eAuthor.get(),self.eYear.get(),self.eISBN.get()))
				self.eTitle.delete(0,END)
				self.eAuthor.delete(0,END)
				self.eYear.delete(0,END)
				self.eISBN.delete(0,END)
		except NameError:
			messagebox.showinfo("Alert", "An entry is not selected to update")

	
#---------End of class Window-------------#

win = Tk()
Window(win)
#looping for holding the screen
win.mainloop()
