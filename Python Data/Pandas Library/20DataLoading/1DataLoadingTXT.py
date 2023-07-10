import pandas as pd
# .txt
# .csv
# .xls
# .xlsx
# json
# and more....

# data loading in text file
# 1.
# text=pd.read_table("TXT.txt")
# print(text)
# print(type(text))
# print(text.columns)
# print(len(text.columns))

# text=pd.read_table("TXT.txt",sep=",")
# print(text)
# print(text.columns)
# print(len(text.columns))

# changing index
# text.set_index('id',inplace=True)
# print(text)
# print(text.values)

# 2.
# df=pd.read_csv("TXT.txt")
# print(df)
# print(type(df))
# print(df.columns)
# print(len(df.columns))

# df=pd.read_csv("TXT.txt",sep=";")
# print(df)
# print(type(df))
# print(df.columns)
# print(len(df.columns))


df=pd.read_csv("TXT1.txt",sep="\t")
print(df)
print(type(df))
print(df.columns)
print(len(df.columns))


df=pd.read_csv("TXT1.txt",sep=";")
print(df)
print(type(df))
print(df.columns)
print(len(df.columns))

