import pandas as pd
# install xlrd package to load
# version 1.2.0

# df=pd.read_excel("C:/Users/best/Downloads/mtcars.xlsx")
# print(df)

# df=pd.read_excel("C:/Users/best/Downloads/mtcars.xlsx",header=None)
# print(df)

# removing heading,skipping first 3 rows,skiping last 3 rows
# df=pd.read_excel("C:/Users/best/Downloads/mtcars.xlsx",skiprows=3,skipfooter=3)
# print(df)

# making 0th column as index,nrows is for how many rows want to read
# only loading 10 rows from excel
# df=pd.read_excel("C:/Users/best/Downloads/mtcars.xlsx",header=None,index_col=0,nrows=10)
# df=pd.read_excel("C:/Users/best/Downloads/mtcars.xlsx",index_col=0,nrows=10)
# print(df)


# to write to excel,install"openpyxl" package
# df.to_excel("test.xlsx",sheet_name="data1",index=False)  # to create a new excel file, to set sheet name,car name column
# print(df)






#titanic file(new cls)
# change to  0 for alive and 1 for not alive
# df.loc[df.alive=="yes","alive"]=0  # resetting values 1 and 2
# df.loc[df.alive=="no","alive"]=1
# print(df.head())
#
# print(df.head(10))


# find the count of peoples who survived based in each embark town
# print(df,loc[df['survived']==1].groupby('embark_town')['survived'].count())

# find the count of people who are not alone gender wise
print(df.loc[df['alone']==False].groupby('sex')['alone'].count())


