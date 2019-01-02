""" 
Program for Dropping Dataframe Columns & Rows using Pandas
		by Aniruddha
"""

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


#drop is not in-place
#0 = row	#1 = column

df2 = df.drop("Address",1) 
print("df.drop(\"Address\",1) : ",df2,"\n",sep="\n")

#	***
#	df.drop("Address",1) : 
#		Name     City       State  Country
#	ID                                        
#	1        Ani  Kolkata    W.Bengal    India
#	2       Jack   London          UK  England
#	3   Michelle    Paris         IDF   France
#	4       John       LA  California      USA
#	5    Charlie  Beijing         B.M    China
#	***


print("df.drop(3,0) : ",df.drop(3,0),"\n",sep="\n") 

#	***
#	df.drop(3,0) : 
#	       Name    Address     City       State  Country
#	ID                                                  
#	1       Ani  3 MG Road  Kolkata    W.Bengal    India
#	2      Jack    89 B.St   London          UK  England
#	4      John  1 Alva St       LA  California      USA
#	5   Charlie  2 Hill St  Beijing         B.M    China
#	***


print("df.drop(df.index[1:4],0) : ",df.drop(df.index[1:4],0),"\n",sep="\n")

#	***
#	df.drop(df.index[1:4],0) : 
#	       Name    Address     City     State Country
#	ID                                               
#	1       Ani  3 MG Road  Kolkata  W.Bengal   India
#	5   Charlie  2 Hill St  Beijing       B.M   China
#	***


print("df.drop(df.columns[1:4],1) : ",df.drop(df.columns[1:4],1),"\n",sep="\n")

#	***
#	df.drop(df.columns[1:4],1) : 
#		Name  Country
#	ID                   
#	1        Ani    India
#	2       Jack  England
#	3   Michelle   France
#	4       John      USA
#	5    Charlie    China
#	***

