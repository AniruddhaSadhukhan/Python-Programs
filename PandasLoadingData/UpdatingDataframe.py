""" 
Program for Updating and Adding Dataframe Columns & Rows using Pandas
		by Aniruddha
"""

#-->LOADING DATAFRAME<--#
import pandas
df = pandas.read_csv("table.csv")
df = df.set_index("ID")
print("df : ",df,"\n",sep="\n")

#	***
#	df : 
#		Name    Address     City       State  Country
#	ID                                                   
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India
#	2       Jack    89 B.St   London          UK  England
#	3   Michelle  9 Chez St    Paris         IDF   France
#	4       John  1 Alva St       LA  California      USA
#	5    Charlie  2 Hill St  Beijing         B.M    China
#	***



#-->ADDING NEW COLUMNS TO DATAFRAME<--#
df["Continent"] = ["Asia","Europe","Europe","N.America","Asia"]
df["Place"] = df.shape[0]*["Earth"]
print("df : ",df,"\n",sep="\n")

#	***
#	df : 
#		Name    Address     City       State  Country  Continent  Place
#	ID                                                                     
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India       Asia  Earth
#	2       Jack    89 B.St   London          UK  England     Europe  Earth
#	3   Michelle  9 Chez St    Paris         IDF   France     Europe  Earth
#	4       John  1 Alva St       LA  California      USA  N.America  Earth
#	5    Charlie  2 Hill St  Beijing         B.M    China       Asia  Earth
#	***


#-->GETTING DIMENSIONS OF DATAFRAME<--#
print("df.shape : ",df.shape,"\n",sep="\n")

#	***
#	df.shape : 
#	(5, 7)
#	***

#-->UPDATING COLUMNS OF DATAFRAME<--#
df["Place"] = df["Country"] + "," + df["Place"]
print("df : ",df,"\n",sep="\n")

#	***
#	df : 
#		Name    Address     City       State  Country  Continent  \
#	ID                                                                 
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India       Asia   
#	2       Jack    89 B.St   London          UK  England     Europe   
#	3   Michelle  9 Chez St    Paris         IDF   France     Europe   
#	4       John  1 Alva St       LA  California      USA  N.America   
#	5    Charlie  2 Hill St  Beijing         B.M    China       Asia   

#		    Place  
#	ID                 
#	1     India,Earth  
#	2   England,Earth  
#	3    France,Earth  
#	4       USA,Earth  
#	5     China,Earth
#	***


#-->DELETING COLUMNS OF DATAFRAME<--#
df.drop(["Place","Continent"],1,inplace=True)
print("df : ",df,"\n",sep="\n")

#	***
#	df : 
#		Name    Address     City       State  Country
#	ID                                                   
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India
#	2       Jack    89 B.St   London          UK  England
#	3   Michelle  9 Chez St    Paris         IDF   France
#	4       John  1 Alva St       LA  California      USA
#	5    Charlie  2 Hill St  Beijing         B.M    China
#	***


#-->ADDING NEW ROWS TO DATAFRAME<--#
df_t = df.T
print("df_t(Transpose of df) : ",df_t,"\n",sep="\n")

#	***
#	df_t(Transpose of df) : 
#	ID               1        2          3           4          5
#	Name           Ani     Jack   Michelle        John    Charlie
#	Address  3 MG Road  89 B.St  9 Chez St   1 Alva St  2 Hill St
#	City       Kolkata   London      Paris          LA    Beijing
#	State     W.Bengal       UK        IDF  California        B.M
#	Country      India  England     France         USA      China
#	***

df_t[6] = ["Ram","5 N.Road","Howrah","W.Bengal","India"]
print("df_t(Transpose of df) : ",df_t,"\n",sep="\n")

#	***
#	df_t(Transpose of df) : 
#	ID               1        2          3           4          5         6
#	Name           Ani     Jack   Michelle        John    Charlie       Ram
#	Address  3 MG Road  89 B.St  9 Chez St   1 Alva St  2 Hill St  5 N.Road
#	City       Kolkata   London      Paris          LA    Beijing    Howrah
#	State     W.Bengal       UK        IDF  California        B.M  W.Bengal
#	Country      India  England     France         USA      China     India
#	***


df = df_t.T
print("df : ",df,"\n",sep="\n")

#	***
#	df : 
#		Name    Address     City       State  Country
#	ID                                                   
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India
#	2       Jack    89 B.St   London          UK  England
#	3   Michelle  9 Chez St    Paris         IDF   France
#	4       John  1 Alva St       LA  California      USA
#	5    Charlie  2 Hill St  Beijing         B.M    China
#	6        Ram   5 N.Road   Howrah    W.Bengal    India
#	***


#-->UPDATING ROWS TO DATAFRAME<--#
df_t = df.T
df_t[3] = ["Michelle","5 H.St","Vizag","A.P","India"]
df = df_t.T
print("df : ",df,"\n",sep="\n")

#	***
#	df : 
#		Name    Address     City       State  Country
#	ID                                                   
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India
#	2       Jack    89 B.St   London          UK  England
#	3   Michelle     5 H.St    Vizag         A.P    India
#	4       John  1 Alva St       LA  California      USA
#	5    Charlie  2 Hill St  Beijing         B.M    China
#	6        Ram   5 N.Road   Howrah    W.Bengal    India
#	***

