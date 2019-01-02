""" 
Program to understand the concept of Object Oriented Programming
	by Aniruddha
"""


class Account:			#Account is a class
	def __init__(self,file):
		self.filepath = file	#instance variable
		with open(file,'r') as f:
			self.balance = int(f.read())
	
	def withdraw(self,amount):
		self.balance -= amount
	
	def deposit(self,amount):
		self.balance += amount
		
	def commit(self):
		with open(self.filepath,'w') as file:
			file.write(str(self.balance))
		

class CheckingAccount(Account):	#Inheritation		
				#doc strings provides explanation of class
	""" 				
	This class generates checking account objects
	"""
	type = "Checking Account"	#type is class variable,shared by all instance of class
	
	def __init__(self,filepath,fee):	#constructor
		Account.__init__(self,filepath)
		self.fee = fee
	
	def transfer(self,amount):		#class method
		self.balance -= (amount+self.fee)
	
	def __del__(self):			#destructor
		print("Destructor called")
		
		

c = CheckingAccount("bal.txt",5)	#c is a object instance
print("Jack:\n",c.type,"\n")		#type :class variable,same for all instance of class
print("Balance:",c.balance)		#balance:instance variable:different for different instance of class
					#both class variable & instance variable are data member of a class
c.deposit(10000)			
print("Deposit(10000):",c.balance)
c.withdraw(5000)
print("Withdraw(5000)",c.balance)
c.transfer(5000)
print("Transfer(5000)",c.balance)
c.commit()


d = CheckingAccount("bal2.txt",5)	#instantiation of class
print("John:\n",d.type,"\n")
print("Balance:",d.balance)
d.deposit(10000)
print("Deposit(10000):",d.balance)
d.withdraw(5000)
print("Withdraw(5000)",d.balance)
d.transfer(5000)
print("Transfer(5000)",d.balance)
d.commit()


print(c.__doc__)
