# 1D array

import numpy as np

# a=np.array([8,2,5,9,11,6])
# print(a)
# print(a[:])
# print(a[2:])
# print(a[2:5])
# print(a[:4])
# print(a[0:6:2])
# print(a[::-1])

##############
# 2D array--> x[strt:end:stp , strt:end:step]

# x=np.array([[1,2],[3,4],[5,6]])
# print(x)
# # for 4,6
# print(x[1:,1:])
# # for 3,4
# print(x[1,:])

y=np.array([[1,2,3,4],[5,6,7,8],[20,30,40,50]])
print(y)
print(y[1:,1:])
print(y[1,1])
print(y[::,::2])

###############
# 3D array--> z[srt:end:stp,srt:end:stp,srt:end:stp] ie,(matrix,rows,columns)

z=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
d=np.array(z)
print(d)
print(d[:,:,:1])  # all matrix,all rows,upto 1st column
print(d[:,1:,::2])



