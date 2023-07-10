# sorting
# there are two kids of sorting available in pandas

import pandas as pd
l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[6,8,9]]
df=pd.DataFrame(l,index=['a','b','c','d','e',],columns=['id','age','mark'])
print(df)

# we can sort by label(index)
dfnew=df.sort_index()
print(dfnew)
dfnew=df.sort_index(ascending=False)
print(dfnew)

# # we can sort by label(column)
dfnew=df.sort_index(axis=1)
print(dfnew)

# we can sort by values,get new dataframe
print(df.sort_values(by='age'))   # must specify by column name
print(df.sort_values(by=['age','mark']))   # we will not get correct sorting
dfnew=df.sort_values(by='age',ascending=False)
print(dfnew)

"""sort_values() provides a provision to choose the algorithm 'mergesort',is the only stable algorithm"""
# pandas supports mergesort
'''
# if we have 5 elements ,split it into two,then sort each part and
# join both and sort it again
##'''


unsorted_df=pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print(unsorted_df)
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')
print(sorted_df)