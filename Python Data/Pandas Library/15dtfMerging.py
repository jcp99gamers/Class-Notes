# merging and joining


import pandas as pd
df1 = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
print(df1)

df2 = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(df2)
# print(right)

# merging dataframes using id
print(pd.merge(df1,df2))
print(pd.merge(df1,df2,on='id'))
# merging data frames using multiple variables
print(pd.merge(df1,df2,on=['id','subject_id']))

"""merging using how(how can have 4 values-left,right,inner,outer)"""
# innerjoin
print(pd.merge(df1,df2,on='subject_id'))

# left
print(pd.merge(df1,df2,on='subject_id',how='left'))
# right
print(pd.merge(df1,df2,on='subject_id',how='right'))
# full outer
print(pd.merge(df1,df2,on='subject_id',how='outer'))
print(pd.merge(df1,df2,how='outer'))
