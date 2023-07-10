import pandas as pd
l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,5,9]]
df=pd.DataFrame(l,index=['a','b','c','d','e','f'],columns=['id','age','mark'])
print(df)

# to add new rows
# df2=pd.DataFrame([[7,10,6],[8,12,8]],columns=['id','age','mark'])
# print(df2)
# df=df.append(df2)
# print(df)

# to delete row
# df=df.drop('f')
# print(df)

# df=df.drop(['a','c'])
# print(df)

# to add new column with all values same
# df['new']=12
# print(df)

# df['new']=df['age']+df['mark']
# print(df)

# to add new column with diff values
# df['new']=[1,2,3,4,5,6]  # the elements and number of rows should match
# print(df)

# to delete any column
# print(df.pop('mark'))
# print(df)
# df1=df.pop('mark')
# print(df1)

# df.drop(['mark'],axis=1)
# print(df)
# df1=df.drop(['mark'],axis=1)  # new df
# print(df1)

# data frame membership,same as in series
# print(df.isin([2,4]))
# print(df[df.isin([2,4])])

# transposes rows and columns
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# create a dataframe
df=pd.DataFrame(d)
print("our data series is:")
print(df)
print(df.shape)

print(df.T)
dfnew=df.T
print(df.shape)
print(dfnew.shape)

a=dfnew.shape[0]
b=dfnew.shape[1]
print(a)
print(b)

