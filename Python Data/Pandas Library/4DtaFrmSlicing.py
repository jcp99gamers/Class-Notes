import pandas as pd
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,5,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],columns=['id','age','mark'])
# print(df)

# print(df['id'])   # to get specific column
# print(df.id)
# print(df[['id','age']])  # to get specific columns

# .loc -->used for custom index
# .iloc -->used for actual/default row index

# to get specific rows,
# print(df.loc['b'])  # used for custom index
# print(df.iloc[1])   # used for actual/default row index

# print(df.loc[['b','f']])  # multiple rows
# print(df.iloc[[1,3]])

# print(df.loc['b':'f'])
# print(df.iloc[0:3])

# print(df.loc[:,['id','age']])  # slicing column and rows
# print(df.iloc[:,[1,2]])

# print(df.loc['b':,['id','age']])
# print(df.iloc[2:,[1,2]])

# print(df.loc[['b','f'],['id','age']])
# print(df.iloc[[1,5],[0,1]])

# print(df.loc['a':'e','id':'age'])
# print(df.iloc[1:4,1:2])

# print(df.iloc[-1,-1])
# print(df.iloc[-1:,-1:])
# print(df.iloc[-3:,-2:])

# to achieve is a single value within a DataFrame ,first you have use the name of the column and
# then the index or the label of the new

# print(df['id']['b'])  # [column][row]

# methods on index--->to get same information about index from a data structure
# print(df.iloc[:,1].idxmax())
# print(df.iloc[:,1].idxmin())



### conditional slicing/filtering method

l=[[1,2,3,'ajith','mech'],[2,5,6,'alex','mech'],[3,8,9,'john','cs'],[4,8,9,'ann','ec'],[5,9,8,'smith','cs']]
df=pd.DataFrame(l,index=['a','b','c','d','e'],columns=['id','age','mark','name','dept'])
print(df)

# print(df['age']>5)
# print(df[df['age']>5])

# print(df['mark']==9)
# print(df[df['mark']==9])
# print(df.loc[df['mark']==9])
# print(df.loc[df.mark==9])
# print(df[df.iloc[:,2]==9])

# with .loc we slicing df,so here we can mention columns as well
# print(df.loc[df.mark>6,"mark"])
# print(df.loc[df.mark>6,["mark","age"]])
# df1=df.loc[df.mark>6,"mark"]
# print(df1)
# print(type(df1))
# dfn1=df.loc[df.mark>6,["mark","age"]]
# print(dfn1)
# dfnew=df[df['mark']>6]
# print(dfnew)


# two conditions using logical operator
# we can't use &
# print((df.mark<=6)&(df.dept=='mech'))
# print(df[(df.mark<=6)&(df.dept=='mech')])
# print(df[(df["mark"]<=6)&(df["dept"]=='mech')])
# print(df.loc[(df["mark"]<=6)&(df["dept"]=='mech')])
# print(df.loc[(df["mark"]<=6)&(df["dept"]=='mech'),"id"])

# print mark b/w 7&9
# print(df[(df.mark>7)&(df.mark<9)])

# print(df[(df.mark<=6)|(df.dept=='mech')])
# print(df[(df.dept=='cs')|(df.dept=='mech')|(df.dept=='ec')])
# print((df.dept.isin(['cs','mech','ec'])))    # boolean
# print(df[df.dept.isin(['cs','mech','ec'])])
# print(df[df.dept.isin(['cs','mech','ec'])&(df.mark<9)])

# assign value
# df["age"]+=2
# print(df)

# df.loc[:,'age']+=2
# print(df)
# df.iloc[:,1]+=3
# print(df)

# df.loc['b']=10
# print(df)
# df.iloc[1]=20
# print(df)

# assign values if a condition satisfies
# print(df.loc[df.mark>6])
# df.loc[df.mark>6,"mark"]=100
# print(df)
# df.loc[df.mark>6]=100  # whole row become 100
# print(df)









