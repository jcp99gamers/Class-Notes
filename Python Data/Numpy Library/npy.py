import numpy as np
arr0 = np.array(0)
arr1 = np.array([0])
arr2 = np.array([[0]])
arr3 = np.array([[[0]]])
arr5 = np.array([0],ndmin=5)# higher dimension arrays
arr9 = np.array([[[[[[[[[0]]]]]]]]])
#Note, Number of Layers of SQUARE BRACKETS Represent the Dimension of the Array...
print(arr5)
print(arr5.ndim)


arrDtObj = np.array([[[123,"STR",5],[1,2.5,3]]],dtype=object)
arrDtNil = np.array([[[123,"STR",5],[1,2.5,3]]])
print(arrDtNil)
print(arrDtObj)
# print(arreg.ndim)


import numpy as np
#Access the third element of the second array of the first array:array indexing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[7, 8, 9], [10, 11, 12]]])
print(arr)

print(arr[1, 1, 2])
# ---------------------------------------------------------------------------------------------
# adding two values in array to 

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3]) 
# -----------------------------------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #1->4
print(arr [::3])
# --------------------------------------------------------------------------------------------
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4:2])#-- 1st is the index values returned of the 2nd  in the  
# -----------------------------------------------------------------
arr = np.array([[1, 2, 3], [4, 5, 6] , [7, 8, 9] , [10, 11, 12], [13, 14, 15]])
print(arr[1:4])
print(arr[1:4, 1:2])
# --------------------------------------------------------------------------------------------
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[7, 8, 9], [10, 11, 12]]])
#-------3dimensional
print(arr)
print("\n")
print(arr[0:2])
print("\n")
print(arr[0:2,1])
print("\n")
print(arr[0:2,1,1])
# ---------------------------------------------------------------------------------
arr = np.array(
    [
        [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            ],
        [
            [16,17,18,19,20],
            [21,22,23,24,25],
            [26,27,28,29,30],
            ],
        [
            [31,32,33,34,35],
            [36,37,38,39,40],
            [41,42,43,44,45],
            ],
        [
            [46,47,48,49,50],
            [51,52,53,54,55],
            [56,57,58,59,60],
            ]
        ]
)
# print(arr)
# print(arr[1:3])
# print(arr[1:3,1:2])
print(arr[1:3,1:2,1:4])
# --------------------------------------------------------------------------------------------  
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],ndmin=3)
# print(arr)
# print(arr[0])
# print(arr[0,0:2])
print(arr[0,0:2,-2])
# --------------------------------------------------------------------------------------------  
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr
z = x
arr[0] = 42
print(arr)
print(x)
print(y)
print(z)
# -----------------------------------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5])
x = arr.view() # x = arr
arr[0] = 42

print(arr)
print(x)
#---------------------------------------------------------------------------------------
arr = np.array([[1, 2, 3, 4],[12,4,6,8],[1,2,3,4]])
print(arr)
print(arr.shape)
# ---------------------------------------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
#-----------------------------------------------------------
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):# similar to for x in arr:for y in x: for z in y
  print(x)

#-------------------------------
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']): # to convert into string data type
  print(x)

# -----------------------------------------
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):  # to specify slicing with step 2
  print(x)
#-------------------------------------------------
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x) #-----------------to print the value with index value along with each value

#----------------------------------------------------------------------------
#join arrays 
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
# -------------------------------------
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
