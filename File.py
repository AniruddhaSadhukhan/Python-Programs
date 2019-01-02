"""
Program to understand file handling
	by Aniruddha
""" 


l = ['Aniruddha', 'Welcome', 'Good Bye']

#Writing in file
f = open("ani.txt",'w')
for i in l:
	f.write(i+"\n")
f.close()





#Reading in file
f = open("ani.txt",'r')
print("Type of f is: ",type(f),"\n")

content = f.read()
print(content)
print("Type of content is: ",type(content),"\n")

content = f.readlines()
print(content,end="\n\n") #file pointer is at end,list will be empty

f.seek(0) #go to begining
content = f.readlines()
print(content)
print("Type of content is: ",type(content),"\n")

#striping \n from strings in list
content = [i.rstrip("\n") for i in content]
print(content,"\n")

#printing length of each line
for i in content:
	print(content.index(i)+1," : ",len(i))
	
f.close()




#Appending in file
f = open("ani.txt",'a')
f.write("Hope you enjoy\n")
f.close()

#use of with : close method not needed
with open("ani.txt",'a+') as f:
	f.seek(0)
	content = f.read()
	f.write("See you next time\n")
print(content,"\n")

with open("ani.txt",'r+') as f:
	print(f.read())
	f.write("Take care\n")
	
with open("ani.txt",'w+') as f:
	f.write("File overwritten as it exists\n")
	f.seek(0)
	print(f.read())

# Sample Output:

#	Type of f is:  <class '_io.TextIOWrapper'> 

#	Aniruddha
#	Welcome
#	Good Bye

#	Type of content is:  <class 'str'> 

#	[]

#	['Aniruddha\n', 'Welcome\n', 'Good Bye\n']
#	Type of content is:  <class 'list'> 

#	['Aniruddha', 'Welcome', 'Good Bye'] 

#	1  :  9
#	2  :  7
#	3  :  8
#	Aniruddha
#	Welcome
#	Good Bye
#	Hope you enjoy
#	 

#	Aniruddha
#	Welcome
#	Good Bye
#	Hope you enjoy
#	See you next time

#	File overwritten as it exists


