""" 
Program to block websites 
	by Aniruddha
	
		**
 Run it as sudo (linux and mac) or admin(windows)
 It can also be set to run at runtime	
"""

import time
from datetime import datetime as dt

#hosts_path = "C:\Windows\System32\drivers\etc\hosts" 	#windows host file location
hosts_path = "/etc/hosts"	#linux and mac

redirect = "127.0.0.1"

with open("website_list.txt",'r') as file:
	website_list = [x.strip() for x in file.readlines()]
print(website_list)


while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,8,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16,0):
		print("Working hours")
		with open(hosts_path,'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")
	else:
		print("Fun time")
		with open(hosts_path,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
				
	time.sleep(300)
