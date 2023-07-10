# if we iterating diff data structures
"""
series- iterating over values(since it is a single array of values)

in df and panels iteration is like dictionary d={'pid':[1,2,3],'name':['book','pen','pencil'],'price':[20,10,5]
# df=pd.DataFrame(d,index=['a','b','c'])
print(df)
DataFrame-iterating over column labels
panel-iterating over item labels
"""
import pandas as pd
d={'pid':[1,2,3],'name':['book','pen','pencil'],'price':[20,10,5]}
df=pd.DataFrame(d,index=['a','b','c'])
print(df)

# iterating over column labels
for col in df:
    print(col)


"""
iteritems()-to iterate over the key(key,value)pairs
iterrows()-iterate over the rows as(index,series)pairs
itertuples()-iterate over the rows as named tuples
"""


for key,value in df.iteritems():
    print(key)
    print(value)

for x in df.iteritems():  # iterating column wise
    print(x)


for row_index,row in df.iterrows():   # iterating row wise
    print(row_index)
    print(row)

for row in df.itertuples():  # iterating rowwise as tuple
    print(row)

