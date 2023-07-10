import pandas as pd
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,5,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],columns=['id','age','mark'])
# print(df)

# print(df.columns)  # to know column names
# print(df.keys())    # to know column names
# print(df.values)    # to get the values
# print(df.index)    # to get index range
# print(df.dtypes)   # to get column wise data types

# print(df.shape)  # to know rows and columns
# print(df.shape[0])
# print(df.shape[1])

# import numpy as np
# a=df.shape[0]
# b=df.shape[1]
# r=np.ones((a,b))
# print(r)

# print(df.head())   # default 5 rows
# print(df.head(3))
# print(df.tail())
# print(df.tail(2))

# print(df.describe())  # to see the summary

# l=[[1,2,3,"ram"],[2,5,6,"manu"],[3,8,9,"sonu"],[4,8,9,"aldrin"],[5,9,8,"amal"],[6,5,9,"jose"]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],columns=['id','age','mark','name'])
# print(df)
# print(df.describe())    # not consider the name only numerical value

"""25th percentile is 2.25 means,25% of values in that column/list
are less than 2.25 and remaining 75% of values are greater than 2.25"""
import numpy as np
# print(np.percentile(df['id'],25))
# print(np.percentile(df['id'],50))
# print(np.percentile(df['id'],75))
# print(np.percentile(df['id'],90))
"""quartiles are 1st quartile=25%
                 2nd quartile=50%
                 3rd quartile=75%"""

# print(df.size)
# print(df.ndim)

# to know how many unique valur in each column,
# it not considering nan values
l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[np.NaN,5,9]]
df=pd.DataFrame(l,index=['a','b','c','d','e','f'],columns=['id','age','mark'])
print(df)

# print(df.nunique())
# print(df.nunique(axis=0))  # column wise
# print(df.nunique(axis=1))  # row wise

# to consider nan also,
# print(df.nunique(dropna=False))

# to count values in a column,
# print(df['age'].value_counts())
# print(df['mark'].value_counts())
