""" 
Program to understand the datetime and time module
		by Aniruddha
"""

import datetime


print ("Current date & time: ",datetime.datetime.now())
print ("Appropriate date & time: ",datetime.datetime.now().strftime("%c"))
print ("Appropriate date : ",datetime.datetime.now().strftime("%x"))
print ("Appropriate time : ",datetime.datetime.now().strftime("%X"))
print ("Current date: ",datetime.datetime.now().strftime("%d-%m-%y"))
print ("Current date: ",datetime.datetime.now().strftime("%d-%b-%Y %a"))
print ("Current day & month: ",datetime.datetime.now().strftime("%A %B "))
print ("Day of the year: ",datetime.datetime.now().strftime("%j"))
print ("Current time(24hr) : ",datetime.datetime.now().strftime("%Hh %Mm %Sss"))
print ("Current time(12hr) : ",datetime.datetime.now().strftime("%Ih %Mm %Ss %p"))


#class datetime.datetime(year,month,day[,hour[,minute[,second[,microseconds[,tzinfo]]]]])
now = datetime.datetime.now()
prev = datetime.datetime(1997,7,21,10)
print("\n\nNow = ",now)
print("Prev = ",prev)
diff = now-prev
print("Difference = ",diff)
print("Difference in days = ",diff.days)
print("Difference in sec = ",diff.total_seconds())
print("Difference in years = ",diff.total_seconds()/(60*60*24*365.25))
print(type(diff))


#class datetime.timedelta([days[,seconds[,microseconds[,milliseconds[,minutes[,hours[,weeks]]]]]]])
print("Adding = ",now+datetime.timedelta(2,4,30))
print("Adding = ",now+datetime.timedelta(days=2,hours=2,minutes=30))


import time

lst=[]
for i in range(5):
	lst.append(datetime.datetime.now())
	time.sleep(0.5)	#delay for 0.5 seconds
for i in lst:
	print (i)
	

#***
#	Current date & time:  2018-01-17 11:57:44.441790
#	Appropriate date & time:  Wed Jan 17 11:57:44 2018
#	Appropriate date :  01/17/18
#	Appropriate time :  11:57:44
#	Current date:  17-01-18
#	Current date:  17-Jan-2018 Wed
#	Current day & month:  Wednesday January 
#	Day of the year:  017
#	Current time(24hr) :  11h 57m 44ss
#	Current time(12hr) :  11h 57m 44s AM


#	Now =  2018-01-17 11:57:44.442325
#	Prev =  1997-07-21 10:00:00
#	Difference =  7485 days, 1:57:44.442325
#	Difference in days =  7485
#	Difference in sec =  646711064.442325
#	Difference in years =  20.49303700035253
#	<class 'datetime.timedelta'>
#	Adding =  2018-01-19 11:57:48.442355
#	Adding =  2018-01-19 14:27:44.442325
#	2018-01-17 11:57:44.451003
#	2018-01-17 11:57:44.951623
#	2018-01-17 11:57:45.452234
#	2018-01-17 11:57:45.952839
#	2018-01-17 11:57:46.453454

#***
