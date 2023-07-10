# methods to create array
# array(),arange(),ones(),zeros(),
# eye(),linspace(),random()

# 1.array()---create array from lists and tuples
import numpy as np
# 1D
# a=np.array([1,2,3])
# print(a)
# a=np.array((1,2,3))
# print(a)
# print(a.ndim)
# print(a.dtype)   # by defualt it takes data type as
                   # minimum type required to hold the objects
# narray=np.array([12,45,78],dtype='int64')
# print(narray.dtype)
# a=np.array([1.0,2.5,3.4])
# print(a)
# print(a.dtype)
# a=np.array([1,2,3.0])
# print(a)
# print(a.dtype)

##########
# 2D
# a=np.array([[1,2],[3,4]])
# print(a)
# print(a.ndim)  # matrix
###########
# 3D
# a=np.array([[[1,2,2],[3,4,4,]],[[5,6,6],[7,8,8]]])
# print(a)
# print(a.ndim)  # 3D array/cube/3D tensor
# print(a.shape)
# multi dim arrays are called tensor

###############################
# 2.arange()---create an array of evenly spaced values
# same like range fn,but return an ndarray
# z=np.arange(10)
# print(z)
# z=np.arange(5.0)
# print(z)
# z=np.arange(2,10)
# print(z)
# z=np.arange(2,10,2)
# print(z)

# z=np.arange(10,dtype='complex')
# print(z)

####################################
# 3.zeros()----create array filled with zeros
# shape should be given as int or tuple of int
# default type is float

# s=np.zeros(5)
# print(s)
# s=np.zeros((3,4))
# print(s)

##################################
# 4.ones()----create array filled with ones
# default type is float

# r=np.ones(5)
# print(r)
# r=np.ones(5,dtype='int')
# print(r)
# r=np.ones((5,2))
# print(r)
#
# r=np.ones((5,2,2))
# print(r)

##############################
# 5.linspace()---create array filled with evenly spaced values
# similar to arange fn,but gives end point also

# a=np.linspace(2,10)   # start and end point
# print(a)   # we get default 50 points

# b=np.linspace(1,10,4)
# print(b)
# # exclude last point
# b=np.linspace(2,10,4,endpoint=False)
# print(b)

#############################
# 6.eye()---gives an array filled with zeros expected kth diagoanal to 1

# a=np.eye(3)   # n=m by default(rows and columns)
# print(a)
# define where we want 1s
# a=np.eye(3,k=2)
# print(a)
# a=np.eye(3,k=-2)
# print(a)

# a=np.eye(3,2)
# print(a)
# same to eye() we have identity fn for sqr matrix
# a=np.identity(5)
# print(a)

#####################################
# 7.random()----for creating a random number array
# fns in random module
# -rand()
# -randn()
# -randint()

# a=np.random.rand(5)   # uniformly distributed 5 random numbers
# print(a)
# a=np.random.rand(5,2)   # uniformly distributed random numbers
# print(a)
# b=np.random.randn(4)   # normal distributed random numbers
# print(b)
# a=np.random.randint(2,6)   # gives a  random number b/w 2&6
# print(a)
# c=np.random.randint(100,size=4)
# print(c)
# c=np.random.randint(100,size=(2,3))
# print(c)