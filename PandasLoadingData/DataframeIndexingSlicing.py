"""
Program for indexing and slicing Dataframes using Pandas
		by Aniruddha
"""
import pandas
df = pandas.read_csv("table.csv")
print("table.csv : ",df,"\n",sep="\n")

#	***
#	table.csv : 
#	   ID      Name    Address     City       State  Country
#	0   1       Ani  3 MG Road  Kolkata    W.Bengal    India
#	1   2      Jack    89 B.St   London          UK  England
#	2   3  Michelle  9 Chez St    Paris         IDF   France
#	3   4      John  1 Alva St       LA  California      USA
#	4   5   Charlie  2 Hill St  Beijing         B.M    China
#	***



#set_index is not in-place
df = df.set_index("ID")
#or use		df.set_index("ID",inplace=True)
print("table.csv : ",df,"\n",sep="\n")

#	***
#	table.csv : 
#		Name    Address     City       State  Country
#	ID                                                   
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India
#	2       Jack    89 B.St   London          UK  England
#	3   Michelle  9 Chez St    Paris         IDF   France
#	4       John  1 Alva St       LA  California      USA
#	5    Charlie  2 Hill St  Beijing         B.M    China
#	***


#LEVEL BASED INDEXING
print("df.loc[2:4,\"Address\":\"State\"] : ",df.loc[2:4,"Address":"State"],"\n",sep="\n")

#	***
#	df.loc[2:4,"Address":"State"] : 
#	      Address    City       State
#	ID                               
#	2     89 B.St  London          UK
#	3   9 Chez St   Paris         IDF
#	4   1 Alva St      LA  California
#	***

print("df.loc[1,\"State\"] : ",df.loc[1,"State"],"\n",sep="\n")

#	***
#	df.loc[1,"State"] : 
#	W.Bengal
#	***


print("df.loc[:,\"Country\"] : ",df.loc[:,"Country"],"\n",sep="\n")

#	***
#	df.loc[:,"Country"] : 
#	ID
#	1      India
#	2    England
#	3     France
#	4        USA
#	5      China
#	Name: Country, dtype: object
#	***


lst = list(df.loc[:,"Country"])
print(lst,"\n\n")

#	***
#	['India', 'England', 'France', 'USA', 'China'] 
#	***



#INDEX BASED INDEXING
print("df.iloc[1:4,1:4] : ",df.iloc[1:4,1:4],"\n",sep="\n")
#as it is upperbound exclusive

#	***
#	df.iloc[1:4,1:4] : 
#	      Address    City       State
#	ID                               
#	2     89 B.St  London          UK
#	3   9 Chez St   Paris         IDF
#	4   1 Alva St      LA  California
#	***


print("df.iloc[0,3] : ",df.iloc[0,3],"\n",sep="\n")

#	***
#	df.iloc[0,3] : 
#	W.Bengal
#	***


print("df.iloc[:,3:] : ",df.iloc[:,3:],"\n",sep="\n")

#	***
#	df.iloc[:,3:] : 
#		 State  Country
#	ID                     
#	1     W.Bengal    India
#	2           UK  England
#	3          IDF   France
#	4   California      USA
#	5          B.M    China
#	***


print("df.iloc[0,3:] : ",df.iloc[0,3:],"\n",sep="\n")

#	***
#	df.iloc[0,3:] : 
#	State      W.Bengal
#	Country       India
#	Name: 1, dtype: object
#	***
