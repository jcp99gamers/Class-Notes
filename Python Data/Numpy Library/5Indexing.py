# indexing in 1D---> 0,1,2,....

import numpy as np
# a=np.array([1,2,3,4,5])
# print(a)

# print(a[0])
# print(a[3])
# print(a[-1])

####################
# 2D array--> it is an array with in an array

# b=np.array([[1,2],[3,4]])
# print(b)

# print(b[0][0])
# print(b[0][1])
# print(b[1][1])
# print(b[-1][0])
# print(b[-1][-1])
# print(b[-2][-2])

#####################
# 3D array---> 2d array in an array

# c=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
# d=np.array(c)
# print(d)
# print(d.ndim)
# print(d[0][1][1])  # [matrix][row][column]
# print(d[1][0][0])
# print(d[1][2][3])

# print(d[-2][-3][-4])  # matrix-1&-2, rows -1,-2,-3, columns -1,-2,-3,-4
# print(d[0])
# print(d[0][1])
# also we can use,
# print(d[0,1,1])
# print(d[0,1])
# print(d[0,:,1])   # 1st column in 0th matrix
# print(d[0,:,:])
# print(d[0,1:,1:])

########################
# assign values

a=np.array([1,2,3,4,5])
print(a)
a[3]=100
print(a)

b=np.array([[1,2],[3,4]])
print(b)
b[0][1]=100
print(b)

c=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
d=np.array(c)
print(d)
d[0][1][1]=100
print(d)
d[0,1:,1:]=111
print(d)

# using arange fn,
# a=np.arange(10)
# print(a)
# a[5:]=10
# print(a)

# b=np.arange(4)
# print(b)
# print(b[::-1])   # reverse

# a[6:]=b[::-1]
# print(a)
