
#Program to understand For Loop
#	by Aniruddha


mylist = []

#input list
for i in range(5):
	mylist.append(i+1)

#printing values in list
for item in mylist:
	print(item,end=" ") 

print("\n")

#printing values in list greater than 2
for item in mylist:
	if item>2:
		print(item) 

print("\n")

#printing values in 2 list only if a string contain a certain substring
names = ["Aniruddha","John","Jack    "]
email = ["ani@gmail.com","john@hotmail.com","jack@gmail.com"]
for i,j in zip(names,email):
	if "@gmail.com" in j:
		print(i,j,sep="\t")
		
		
		
		
		
#Sample Output:
#1 2 3 4 5 

#3
#4
#5


#Aniruddha	ani@gmail.com
#Jack    	jack@gmail.com


