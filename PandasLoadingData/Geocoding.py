"""
Program for Geocoding on Dataframes using Pandas & Geopy
		by Aniruddha
		
Install Geopy by : sudo pip3 install geopy
"""


import pandas
df = pandas.read_csv("geodata.txt").set_index("ID")
print("df:",df,"\n",sep="\n")

#***
#	df:
#		Name          Address           City               State Country
#	ID                                                                      
#	1        Ani      8 M.G. Road        Kolkata  West Bengal 700006   India
#	2       Jack     3666 21st St  San Francisco            CA 94114     USA
#	3   Michelle      332 Hill St  San Francisco    California 94114     USA
#	4       John     3995 23rd St  San Francisco            CA 94114     USA
#	5    Charlie  551 Alvarado St  San Francisco            CA 94114     USA
#***

from geopy.geocoders import Nominatim
nom = Nominatim(scheme="http")


#EXAMPLE
n = nom.geocode("3666 21st St, San Francisco, CA 94114,USA")
if n!=None:
	print(n.latitude,",",n.longitude)
#***
#	37.7570511 , -122.4188036
#***

#APPLYING ON THE DATAFRAME COLUMNS
df["Coordinates"] = df["Address"] + "," + df["City"] + ", " + df["State"] + ", " + df["Country"]
df["Coordinates"] = df["Coordinates"].apply(nom.geocode).apply(lambda x:(str(x.latitude) + "," +str(x.longitude))  if x!=None else None)
print("df:",df,"\n",sep="\n")

#***
#	df:
#		Name          Address           City               State Country  \
#	ID                                                                         
#	1        Ani      8 M.G. Road        Kolkata  West Bengal 700006   India   
#	2       Jack     3666 21st St  San Francisco            CA 94114     USA   
#	3   Michelle      332 Hill St  San Francisco    California 94114     USA   
#	4       John     3995 23rd St  San Francisco            CA 94114     USA   
#	5    Charlie  551 Alvarado St  San Francisco            CA 94114     USA   

#		        Coordinates  
#	ID                           
#	1                      None  
#	2   37.7570511,-122.4188036  
#	3     37.756102,-122.421041  
#	4   37.7529648,-122.4317141  
#	5      37.753666,-122.43444 
#***
