# data structures in pandas
# 1.series--1D array(capable of holding data of any type)
# 2.DataFrame--2D labelled tabular structure with heterogeneously typed columns
# 3.panel--3D labeled array

import pandas as pd # pip install pandas
# series data structure
## series can be created in following ways

# 1.from a scalar value(a constant value)

s1=pd.Series(10)
print(s1)
print(type(s1))

# s1=pd.Series(10,dtype='int32') # change datatype
# print(s1)
# print(type(s1))

# s2=pd.Series(10,index=[1,2,3,4])  # custom indexing
# print(s2)
# print(type(s2))

# s2=pd.Series(10,index=['a','b','c'])
# print(s2)
# print(type(s2))

########################
# 2.from a list

s1=pd.Series([10,20,30,"ah"])
print(s1)

# s2=pd.Series([10,20,30],index=['a','b','c'])
# print(s2)

##########################
# 3.from a dictionary
# d={'x':100,'y':200,'z':300}
# s1=pd.Series(d)
# print(s1)
########################
# 4.from numpy 1D array
# import numpy as np
# a=np.array([4,5,6])
# s1=pd.Series(a)
# print(s1)

# s1=pd.Series(a,index=['a','b','c'])
# print(s1)

# print(s1[1])
# print(s1[0])
# print(s1[:])
# print(s1[-1])
# print(s1[:-1])
# print(s1[::2])
# print(['a'])
# s1['a']=100
# print(s1)

########################
# attributes applicable in series

# s1=pd.Series([10,20,30,"ah"],index=['a','b','c','d'])
# print(s1)
# print(s1.dtype)
# print(s1.size)
# print(s1.shape)
# # print(s1.data)  # get a warning
# print(s1.ndim)
# print(s1.itemsize)  # get an error

###############################
# sorting
# s1=pd.Series([10,20,30,50],index=['a','b','c','d'])
# print(s1)
# # we can sort index
# s=s1.sort_index()
# print(s)
# s=s1.sort_index(ascending=False)
# print(s)
# # we can sort values
# print(s1.sort_values())

######################
# can have duplicate values
# serd=pd.Series(range(6), index=['white','white','blue','green','green','yellow'])
# print(serd)
# print(serd['white'])
# # to check any duplicate in index,
# print(serd.index.is_unique)

###########################
# filtering
# s=pd.Series([12,-4,7,9,7],index=['a','b','c','d','e'])
# print(s)
# print(s > 8)
# print(s[s > 8])
# k=[s > 8]
# print(k)
# unique values,
# print(s.unique())
# to count unique values,
# print(s.value_counts())
# evaluates the membership,
# print(s.isin([12, 7, 30]))
# print(s[s.isin([12, 7, 30])])

##############################
# NAN-(not a number)
# is used to within pandas data structure to indicate the presence of an empty field or
# not definable numerically

# import numpy as np
# s2=pd.Series([5,-3,np.NaN,14])
# print(s2)
# isnull(),and notnull() fns are very useful to identify the indexes without a value
# print(s2.isnull())
# print(s2[s2.isnull()])
# print(s2.notnull())
# print(s2[s2.notnull()])

##############################
# fltering from series using keys
# mydict={'red':2000,'blue':1000,'yellow':500,'orange':1000}
# myseries=pd.Series(mydict)

# colors=['red','yellow','orange','blue','green']

# myseries1=pd.Series(myseries,index=colors)
# print(myseries1)

# colors=['red','yellow','orange']
# myseries1=pd.Series(myseries,index=colors)
# print(myseries1)

#############################
# adding two series
# mydict={'red':2000,'blue':1000,'yellow':500,'orange':1000}
# myseries1=pd.Series(mydict)
# print(myseries1)

# mydict2={'red':200,'yellow':1000,'black':700}
# myseries2=pd.Series(mydict2)
# print(myseries2)

# print(myseries1+myseries2)

########################
# attributes
# dict={'red':2000,'blue':1000,'yellow':500,'orange':1000,'red1':2000,'blue1':1000}
# s=pd.Series(dict)
# print(s)
# print("the axis are:")
# print(s.axes)
# print(s.dtype)
# print(s.ndim)
# print(s.size)
# print(s.values)
# print(s.head())  # default value shows first 5 rows
# print(s.head(2))  # first two rows
# print(s.tail())   # last 5 rows
# print(s.tail(2))
# print(s.empty)

################################
