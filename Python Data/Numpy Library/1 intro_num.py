# numpy,pandas,scipy are libraries used for data exploration and analysis
# numpy provides linear algebra and statistical computing fns,mainly for numerical opertaions
# why Numpy&Scipy ->to perform basic scientific/statistical operations like:
#                 ->arrays,matrices,statistics,integration,difff.eqn solver etc
#                 ->but python can perform only some basic mathematical operations
#                 ->so we use these libraries


# Numpy stands for 'Numerical Python'
# data stores in numpy in numpy as 'ndarray' objects

# LIST vs ARRAY
# internally it contains lists
# array is same like list to store data
# both are mutable,indexed
# both can be sliced/slicing operation
###Differences:
# list contains diff datatypes,but array can have elements of same datatypes
# we uses arrays mainly due to need less memory than list,faster than list,convenient to use
# we can perform operations (+,*,etc)directly to an array,but we cant do on this list
# for numpy we want to install Numpy,but list is built_in


import numpy as np # pip install numpy
# memory consumed
# import numpy as np
import sys
s=range(100)   # list
print(s)
print(sys.getsizeof(s))
print(sys.getsizeof(s)*len(s))   # total size=

a=np.arange(100)
print(a)
print(a.size)
print(a.itemsize)
print(a.size*a.itemsize)
