""" 
Program to implement a python script to merge all txt files in directory
			by Aniruddha
			
Here a 3rd party module (glob2) is used.
-->Steps for installing: (on Linux)
	 sudo apt-get install python3-pip
	 pip3 install glob2

"""

import glob2
list = glob2.glob("*.txt")
print("-->Files to be merged are:")
for i in list:
	print(i)

for i in list:
	with open(i,"r") as file:
		print("\n-->Content in ",i," : ",file.read())	


import datetime

filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f.txt")
print("\n-->Merged content is being stored in : ",filename)

with open(filename,"w+") as file:
	for item in list:
		with open(item,'r') as f:
			file.write(f.read())
	file.seek(0)
	print("\n-->Content in merged file : ",file.read(),sep="\n")


#***
#	-->Files to be merged are:
#	File1.txt
#	File2.txt
#	File3.txt

#	-->Content in  File1.txt  :  Content 1


#	-->Content in  File2.txt  :  Content 2


#	-->Content in  File3.txt  :  Content 3


#	-->Merged content is being stored in :  2018-01-17-12-04-38-414070.txt

#	-->Content in merged file : 
#	Content 1
#	Content 2
#	Content 3
#***

