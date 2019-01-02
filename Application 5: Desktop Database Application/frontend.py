""" 
Program to design a Desktop Database Appliction
in Python using tkinter and sqlite3 
for maintaining a Bookstore database and 
add,search,delete,update and view book information
	
	by Aniruddha
	
-->For making a standalone application :
	1)Install pyinstaller(pip install pyinstaller)
	2)Run: pyinstaller filename.py
	
~~~~~~~~~~~FrontEnd Part~~~~~~~~~~~~
"""
 
#~~~~~~~~Building GUI~~~~~~~~#

import backend
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


#defines what happens when a entry is selected
def get_selected_row(event):
	global selection_id 
	selection_tuple = listbox.item(listbox.selection()[0],'values')
	selection_id = selection_tuple[0]
	entryboxes = [eTitle,eAuthor,eYear,eISBN]
	for e,data in zip(entryboxes,selection_tuple[1:]):
		e.delete(0,END)
		e.insert(0,data)


#wrapper function for view
def view_command():
	for row in listbox.get_children():
		listbox.delete(row)
	for row in backend.view():
		listbox.insert('','end',values=row)


#wrapper function for search
def search_command():
	for row in listbox.get_children():
		listbox.delete(row)
	for row in backend.search(eTitle.get(),eAuthor.get(),eYear.get(),eISBN.get()):
		listbox.insert('','end',values=row)


#wrapper function for inserting
def insert_command():
	if eTitle.get()=="" or eAuthor.get()=="" or eYear.get()=="" or eISBN.get()=="": 
		messagebox.showinfo("Alert", "Enter all the fields")
	else:backend.insert(eTitle.get(),eAuthor.get(),eYear.get(),eISBN.get())
	for row in listbox.get_children():
		listbox.delete(row)
	listbox.insert('','end',values=("",eTitle.get(),eAuthor.get(),eYear.get(),eISBN.get()))


#wrapper function for deleting
def delete_command():
	try:
		backend.delete(selection_id)
		listbox.delete(listbox.selection())
		eTitle.delete(0,END)
		eAuthor.delete(0,END)
		eYear.delete(0,END)
		eISBN.delete(0,END)
	except NameError:
		messagebox.showinfo("Alert", "An entry is not selected to delete")


#wrapper function for updating
def update_command():
	try:
		if eTitle.get()=="" or eAuthor.get()=="" or eYear.get()=="" or eISBN.get()=="": 
			messagebox.showinfo("Alert", "Enter all the fields")
		else:
			backend.update(selection_id,eTitle.get(),eAuthor.get(),eYear.get(),eISBN.get())
			index = listbox.index(listbox.selection())
			listbox.delete(listbox.selection())
			listbox.insert('',index,values=(selection_id,eTitle.get(),eAuthor.get(),eYear.get(),eISBN.get()))
			eTitle.delete(0,END)
			eAuthor.delete(0,END)
			eYear.delete(0,END)
			eISBN.delete(0,END)
	except NameError:
		messagebox.showinfo("Alert", "An entry is not selected to update")


#creating the window
win = Tk()
win.title("BookStore Management Software by Aniruddha")


#Creating the labels
lTitle = Label(win,text = "Title")
lTitle.grid(row =1,column=1)

lYear = Label(win,text = "Year")
lYear.grid(row =2,column=1)

lAuthor = Label(win,text = "Author")
lAuthor.grid(row =1,column=5)

lISBN = Label(win,text = "ISBN")
lISBN.grid(row =2,column=5)



#Creating the entryboxes
eTitle = Entry(win)
eTitle.grid(row = 1, column = 2,columnspan = 3)

eYear = Entry(win)
eYear.grid(row = 2, column = 2,columnspan = 3)

eAuthor = Entry(win)
eAuthor.grid(row = 1, column = 6,columnspan = 2)

eISBN = Entry(win)
eISBN.grid(row = 2, column = 6,columnspan = 2)



#Creating the box listing the books(ttk.Treeview)
listbox_headers = ["ID","Title","Author","Year",'ISBN']
listbox_width = [24,150,110,40,111]
listbox = ttk.Treeview(win,height=6,columns=listbox_headers ,show = "headings")
for col,wid in zip(listbox_headers,listbox_width):
	listbox.heading(col,text=col)
	listbox.column(col,width=wid,stretch=0)
listbox.grid(row =3,column=1,columnspan = 5,rowspan =6,sticky = "ns")


#Creating the scrollbars for the list of books(ttk.Treeview)
yscroll = Scrollbar(win)
yscroll.grid(row =3,column=6,rowspan =6,sticky="ns")

xscroll = Scrollbar(win,orient = HORIZONTAL)
xscroll.grid(row =9,column=1,columnspan = 5,sticky="ew")


#configure scrollbars and list for synchronisation
listbox.configure(yscrollcommand = yscroll.set)
yscroll.configure(command = listbox.yview)

listbox.configure(xscrollcommand = xscroll.set)
xscroll.configure(command = listbox.xview)


#binding event to the list
listbox.bind('<<TreeviewSelect>>',get_selected_row)


#creating the buttons for different functions
bView = Button(win,text = "View All",width=12,command = view_command)
bView.grid(row =3,column=7)

bSearch = Button(win,text = "Search",width=12,command = search_command)
bSearch.grid(row =4,column=7)

bAdd = Button(win,text = "Add Entry",width=12,command = insert_command)
bAdd.grid(row =5,column=7)

bUpdate = Button(win,text = "Update Selected",width=12,command = update_command)
bUpdate.grid(row =6,column=7)

bDelete = Button(win,text = "Delete Selected",width=12,command = delete_command)
bDelete.grid(row =7,column=7)

bClose = Button(win,text = "Close",width=12,command = win.destroy)
bClose.grid(row =8,column=7)


#configuring the rows and columns for extra spacing
win.grid_rowconfigure(0,minsize = 20)
win.grid_rowconfigure(9,minsize = 1)
win.grid_rowconfigure(10,minsize = 20)
for r in range(9):
	win.grid_rowconfigure(r,pad = 10)
win.grid_columnconfigure(0,minsize = 30)
win.grid_columnconfigure(8,minsize = 30)

win.grid_columnconfigure(6,weight = 1)
win.grid_columnconfigure(7,weight = 100)


#looping for holding the screen
win.mainloop()
