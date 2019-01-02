"""
Program to get started with Pandas
	by Aniruddha
"""

import pandas

df1 = pandas.DataFrame([[2,4,6],[20,50,100]])
print(df1,"\n\n")

#	***
#	    0   1    2
#	0   2   4    6
#	1  20  50  100 
#	***


df2 = pandas.DataFrame([[2,4,6],[20,50,100]],columns = ["A","B","C"],index=["First","Second"])
print(df2,"\n\n")

#	***
#		 A   B    C
#	First    2   4    6
#	Second  20  50  100 
#	***


df3 = pandas.DataFrame([{"Name":"Aniruddha","Surname":"Sadhukhan"},{"Surname":"Reacher","Name":"Jack"}])
print(df3,"\n\n")

#	***
#		Name    Surname
#	0  Aniruddha  Sadhukhan
#	1       Jack    Reacher 
#	***


print("Type of df2: ",type(df2),"\n\n")

#	***
#	Type of df2:  <class 'pandas.core.frame.DataFrame'> 
#	***


print("Mean of Columns:",df2.mean(),"\n",sep="\n")

#	***
#	Mean of Columns:
#	A    11.0
#	B    27.0
#	C    53.0
#	dtype: float64
#	***


print("Type of df2.mean(): ",type(df1.mean()),"\n\n")

#	***
#	Type of df2.mean():  <class 'pandas.core.series.Series'> 
#	***


print("Mean of mean of Columns: ",df2.mean().mean(),"\n\n")

#	***
#	Mean of mean of Columns:  30.3333333333
#	***


print("df2.B:",df2.B,"\n",sep="\n")
print("Type of df2.B: ",type(df2.B),"\n\n")

#	***
#	df2.B:
#	First      4
#	Second    50
#	Name: B, dtype: int64
#
#
#	Type of df2.B:  <class 'pandas.core.series.Series'>
#	***


print("mean of column B: ",df2.B.mean(),"\n\n")

#	***
#	mean of column B:  27.0
#	***
