""" 
Program to design a GUI based application using tkinter
to convert weights in kg to other units
	by Aniruddha
	
"""
from tkinter import *

#Creating the Window
win = Tk()
win.title("Weight Conversion by Aniruddha")

#defining the function to convert weights and provide output
def Conv():
	
	#making textbox editable
	t1.configure(state = 'normal')
	t2.configure(state = 'normal')
	t3.configure(state = 'normal')
	
	#deleting previous texts in textbox
	t1.delete("1.0",END)
	t2.delete("1.0",END)
	t3.delete("1.0",END)
	
	try:
		kg = float(e1.get())
		#if blank or invalid input is given exception is thrown
		
		#insert the output in textboxes correct upto 2 places after decimal
		t1.insert(END,"%.2f grams"%(kg * 1000))
		t2.insert(END,"%.2f pounds"%(kg * 2.20462))
		t3.insert(END,"%.2f ounces"%(kg * 35.274))
		
		
	except ValueError:
		t1.insert(END,"  ~Invalid Input~")
		t2.insert(END,"  ~Invalid Input~")
		t3.insert(END,"  ~Invalid Input~")
		
	#making textbox uneditable
	t1.configure(state = 'disabled')
	t2.configure(state = 'disabled')
	t3.configure(state = 'disabled')
		


#Creating a Label	
l1 = Label(win,text="Enter weight in Kg:")
l1.grid(row = 1, column = 1,columnspan = 2)


#Creating the Entry Box to give Input
e1 = Entry(win)
e1.grid(row = 1, column = 3,columnspan = 2)


#Creating a button,which when pressed execute the Conv function
b1 = Button(win,text = "Convert",command = Conv)
b1.grid(row = 2, column = 2,columnspan = 2,rowspan = 2)


#Creating 3 text box to show output and 
#disabling them so that users cant edit them
t1 = Text(win,height = 1,width = 20,state = 'disabled')
t1.grid(row = 4, column = 2,rowspan = 1,columnspan = 2)

t2 = Text(win,height = 1,width = 20,state = 'disabled')
t2.grid(row = 5, column = 2,columnspan = 2)

t3 = Text(win,height = 1,width = 20,state = 'disabled')
t3.grid(row = 6, column = 2,columnspan = 2)


#making sure blank spaces are shown in the GUI
for r in range(8):
	win.grid_rowconfigure(r,minsize = 30)
for c in range(6):
	win.grid_columnconfigure(c,minsize = 50)


#must be last statement to hold the GUI
win.mainloop()
