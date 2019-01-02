#Program to find length of any string.
#	by Aniruddha

def Length(s):
	if type(s)==int:
		return "Sorry integers dont have length"
	elif type(s)==float:
		return "Sorry floats dont have length"
	
	else:
		return len(s)

String = input("Please enter a string: ")
print("Length of string is : ",Length(String))
Integer = int(input("Please enter a integer: "))
print(Length(Integer))
Float = float(input("Please enter a float: "))
print(Length(Float))

#***
#	Please enter a string: Aniruddha
#	Length of string is :  9
#	Please enter a integer: 5
#	Sorry integers dont have length
#	Please enter a float: 5.26
#	Sorry floats dont have length
#***

