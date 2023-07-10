# 3writing to csv.py
import pandas as pd
# data={'name':['tom','jack','steve','ricky'],'age':[28,34,29,42]}
# df=pd.DataFrame(data)
# print(df)
# df.to_csv("data.csv")
# df.to_csv("data.csv",index=False)  # providing index=false for avoiding the second time index creation,

# s=pd.read_csv("data.csv")
# print(s)

# s=pd.read_csv("data.csv",header=None) # to avoid column heading
# print(s)
# s=pd.read_csv("data.csv",header=1) # to make 1st row as column name
# print(s)
# print(s.columns)



# diff loading method :using os module
# df=pd.read_csv("C:\\Users\\best\Downloads\\Salary_Data.CSV")
# print(df)

# we can change directory by os module
# import os
# os.chdir("C:\\Users\\best\Downloads")
# print(os.getcwd())
# df=pd.read_csv("Salary_Data.CSV")
# print(df)



# creating csv from text file


