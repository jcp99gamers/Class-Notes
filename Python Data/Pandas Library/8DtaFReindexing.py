# dataframe reindexing
import pandas as pd
import numpy as np
# reindex_like (it makes df index similar to matching df)
# (fill with nan or remove rows if any mismatch)
# df1=pd.DataFrame(np.random.randn(10,4),columns=['col1','col2','col3','col4'])
# df2=pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
# print(df1)
# print(df2)
# df1=df1.reindex_like(df2)
# print(df1)

# filling while reindexing
# print(df2.reindex_like(df1,method='ffill'))  # fill with last row

# limits on filling while reindexing
# print(df2.reindex_like(df1,method='ffill',limit=1))

###############################
# if the df is custom labeled,it replace with another dta frm index position and name
# df=pd.DataFrame({"name":["ann","anu","jiss"],"age":[15,48,26],"marks":[45,78,25]},index=["D","E","A"])
# print(df)
# df1=pd.DataFrame({"name":["anju","kiran","amy"],
#                   "age":[15,14,19],
#                   "marks":[45,85,62]},index=["D","B","A"])
#
# print(df1)
# data=df.reindex_like(df1)
# print(data)

# df=df.reindex(["A","E","C","B"])
# print(df)
# to reindex column
# df=df.reindex(columns=["age","marks","name"])
# print(df)

##############################
# to set date dinamically as index or something like this .we can set datedata as index
datedata=pd.date_range(start="10/1/2019",end="10/4/2019")
print(datedata)
df2=pd.DataFrame({"name":["anju","kiran","amy"],
                  "age":[15,14,19],
                  "marks":[45,85,62]},index=datedata)
print(df2)
