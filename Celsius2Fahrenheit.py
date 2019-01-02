#Program to convert Celsius degrees to Fahrenheit
#	by Aniruddha

def C2F(c):
	 if c<-273.15:
	 	return "Lowest possible temperature is -273.15 °C"
	 else:
	 	return c*9/5 + 32

n = int(input("How many temperatures you want to convert? : "))

Celsius = []
Fahrenheit = []

#The input() function takes only one string argument.
#The {} placeholders are replaced by the arguments to .format()
for i in range(n):
	Celsius.append(float(input("Please enter temperature {} in Celsius: ".format(i+1))))

for i in range(n):
	Fahrenheit.append(C2F(Celsius[i]))

print("Celsius Fahrenheit")

for i,j in zip(Celsius,Fahrenheit):
	print(i,"\t",j)
	



#Sample Output:
#How many temperatures you want to convert? : 4
#Please enter temperature 1 in Celsius: 10
#Please enter temperature 2 in Celsius: -20
#Please enter temperature 3 in Celsius: -289
#Please enter temperature 4 in Celsius: 100
#Celsius Fahrenheit
#10.0 	 50.0
#-20.0 	 -4.0
#-289.0	 Lowest possible temperature is -273.15 °C
#100.0 	 212.0

