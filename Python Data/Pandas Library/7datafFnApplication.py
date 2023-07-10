# there are 3 fn application

# 1.table wise fn application
import pandas as pd
import numpy as np
# def adder(e1e1,e1e2):
#     print(e1e1)
#     print(e1e2)
#     return e1e1+e1e2

# df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# print(df)
# print(df.pipe(adder,2))     # pipe passing df and 2 as arguments and call the fn

# 2.row or column wise fn application
# arbiterary fn can be applied along the axis of dataframe
# we will gwt single values per column/row

# df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# print(df)
# print(df.apply(np.mean))
# print(df.apply(np.mean,axis=1))
# print(df.apply(lambda x: x.max()-x.min()))
# print(df.apply(lambda x: x.max()-x.min(),axis=1))

# 3.element wise fn application
# can perform operation each elements in a column /whole data
# df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# print(df)
# My custom fn
# print(df['col1'].map(lambda x:x*100))  # for single column
# print(df.col1.map(lambda x:x*100))  # same as above
# print(df.iloc[1].map(lambda x:x*100))   # for single row
# print(df.applymap(lambda x:x*100))   # for all data frame elements

##############################
# eg of map
# d = {'Name':pd.Series(['tom','james','ricky','vin','steve','smith','jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23])}
# df=pd.DataFrame(d)
# print(df)
# # finding name starts with s
# print(df.Name.map(lambda x:x.startswith("s")))
# print(df[df.Name.map(lambda x:x.startswith("s"))])
# print(df.loc[df.Name.map(lambda x:x.startswith("s"))])


