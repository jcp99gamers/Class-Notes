# import numpy as np
# transpose of a matrix

# x=np.array([[1,2,3],[5,6,7]])
# print(x)
# print(x.T)

##########
# 1.flattening
# x=np.array([[1,2,3],[5,6,7]])
# print(x)
# print(x.ravel())
# print(np.ravel([[1,2],[5,6]]))

##############
# 2.reshape
# a=np.arange(24)
# print(a)
# print(a.reshape(6,4))  # 2D array
# b=a.reshape((6,2,2)) # 3D array
# print(b.shape)
# print(b)
# c=b.reshape((6,4))
# print(c)

################
# 3.resizing  (fill with zero)
# a=np.arange(4)
# print(a)
# a.resize(8)
# print(a)
# b=a   # false
# a.resize(2,5)
# print(a)

##########
# 4.sorting
# a=np.array([[5,4,6],[2,3,2]])
# print(a)
# b=np.sort(a)
# print(b)

# b=np.sort(a,axis=0) # column wise
# print(b)

# print(a)
# a.sort(axis=1)
# print(a)

# argsort=to get array of index position of a array after sorting
# a=np.array([40,30,10,20])
# print(a)
# d=np.argsort(a)
# print(d)   # it contains index position

#####################

"""25th percentile is 2.25 means,25% of values in that column/list
are less than 2.25 and remaining 75% of values are greater than 2.25"""
a=[10,20,40,80,20,60,50,90,100,110,250,112,10]
import numpy as np
print(np.percentile(a,25))
print(np.percentile(a,50))
print(np.percentile(a,75))
print(np.percentile(a,90))
"""quartiles are 1st quartile=25%
                 2nd quartile=50%
                 3rd quartile=75%"""