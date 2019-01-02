"""
Program to load Dataframes from different files using Pandas
		by Aniruddha
"""

import os
print(os.listdir(),"\n")

#	***
#	['LoadingDataPandas.py', 'table-commas.txt', 'table-semicolons.txt', 'table.csv', 'table.json', 'table.xlsx'] 
#	***


import pandas
df1 = pandas.read_csv("table.csv")
print("table.csv:",df1,"\n",sep="\n")

#	***
#	table.csv:
#	   ID      Name    Address     City       State  Country
#	0   1       Ani  3 MG Road  Kolkata    W.Bengal    India
#	1   2      Jack    89 B.St   London          UK  England
#	2   3  Michelle  9 Chez St    Paris         IDF   France
#	3   4      John  1 Alva St       LA  California      USA
#	4   5   Charlie  2 Hill St  Beijing         B.M    China
#	***


df2 = pandas.read_csv("table-commas.txt")
print("table-commas.txt:",df2,"\n",sep="\n")

#	***
#	table-commas.txt:
#	   ID      Name    Address     City       State  Country
#	0   1       Ani  3 MG Road  Kolkata    W.Bengal    India
#	1   2      Jack    89 B.St   London          UK  England
#	2   3  Michelle  9 Chez St    Paris         IDF   France
#	3   4      John  1 Alva St       LA  California      USA
#	4   5   Charlie  2 Hill St  Beijing         B.M    China
#	***


df3 = pandas.read_csv("table-semicolons.txt",sep=";")
print("table-semicolons.txt:",df3,"\n",sep="\n")

#	***
#	table-semicolons.txt:
#	   ID      Name    Address     City       State  Country
#	0   1       Ani  3 MG Road  Kolkata    W.Bengal    India
#	1   2      Jack    89 B.St   London          UK  England
#	2   3  Michelle  9 Chez St    Paris         IDF   France
#	3   4      John  1 Alva St       LA  California      USA
#	4   5   Charlie  2 Hill St  Beijing         B.M    China
#	***



df4 = pandas.read_json("table.json")
print("table.json:",df4,"\n",sep="\n")

#	***
#	table.json:
#	     Address     City  Country  ID      Name       State
#	0  3 MG Road  Kolkata    India   1       Ani    W.Bengal
#	1    89 B.St   London  England   2      Jack          UK
#	2  9 Chez St    Paris   France   3  Michelle         IDF
#	3  1 Alva St       LA      USA   4      John  California
#	4  2 Hill St  Beijing    China   5   Charlie         B.M
#	***



df5 = pandas.read_excel("table.xlsx",sheet_name=0)
print("table.xlsx:",df4,"\n",sep="\n")

#	***
#	table.xlsx:
#	     Address     City  Country  ID      Name       State
#	0  3 MG Road  Kolkata    India   1       Ani    W.Bengal
#	1    89 B.St   London  England   2      Jack          UK
#	2  9 Chez St    Paris   France   3  Michelle         IDF
#	3  1 Alva St       LA      USA   4      John  California
#	4  2 Hill St  Beijing    China   5   Charlie         B.M
#	***



df6 = df5.set_index("ID")
print("Setting ID as Index:",df6,"\n",sep="\n")

#	***
#	Setting ID as Index:
#		Name    Address     City       State  Country
#	ID                                                   
#	1        Ani  3 MG Road  Kolkata    W.Bengal    India
#	2       Jack    89 B.St   London          UK  England
#	3   Michelle  9 Chez St    Paris         IDF   France
#	4       John  1 Alva St       LA  California      USA
#	5    Charlie  2 Hill St  Beijing         B.M    China
#	***



