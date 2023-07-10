import numpy as np
# operations=== operations are elements

# 1.scalar addition
# a=np.array([10,20,30,40,50])
# print(a+1)

#########
# 2.scalar multiplication
# a=np.array([10,20,30,40,50])
# print(a*2)

########
# 3.scalar exponent
# a=np.array([10,20,30,40,50])
# print(a**2)

########
# 4,=.scalar difference
# a=np.array([10,20,30,40,50])
# print(a-2)

###########################################
# operations b/w arrays are also element wise
# a=np.array([10,20,30,40,50])
# b=np.ones(5)+1
# print(b)
# print(a-b)

# a1=np.array([[1,2],[3,4]])
# a2=np.array([[1,2],[3,4]])
# print(a1)
# print(a2)
# print("sum",a1+a2)
# print("mul",a1*a2)     # element wise multiplication
# print("matx",a1.dot(a2))   # actual matrix multiplication

###################
# comparison operators
# 1)element wise
# a=np.array([1,2,3,4])
# b=np.array([5,2,3,6])
# print(a==b)
# print(a>b)

# 2)array wise
# a=np.array([1,2,3,4])
# b=np.array([5,2,3,6])
# c=np.array([1,2,3,4])
# print(np.array_equal(a,b))
# print(np.array_equal(a,c))

################################
# trancdental functions
# combination of the algebraic operations of addition,substraction,multiplication

# a=np.arange(5)
# print(a)
# print(np.sin(a))
# print(np.log(a))
# print(np.sqrt([2,5,8]))
# shape mismatch
# a=np.arange(5)
# b=np.arange(2)
# print(a+b)

################
# basic reduction
# arr=np.array([10,20,30,40,50])
# print(arr.sum())
# print(np.sum(arr))
# print(arr.max())
# print(np.max(arr))
# print(arr.min())
# print(np.min(arr))

# print(arr.argmax())   #  index of max element(find greatest value position)
# print(arr.argmin())  # index of min element(find small value positon)

# x=np.array([[1,1],[2,2]])
# print(x)
# print(x.sum())
# print(x.sum(axis=0)) # column ##important
# print(x.sum(axis=1))  # row

#############################
# statistics
# x=np.array([1,2,3,1])
# x=np.array([[1,2,3],[5,6,7]])
# print(x.mean())  # it is the avg value
# print(np.mean(x))
# print(np.median(x))  # it gives central value from sorted order.it will not affect much if any value changes lot
# print(x.std())   # standard deviation


