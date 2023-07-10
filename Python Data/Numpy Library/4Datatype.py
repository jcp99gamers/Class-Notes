# numerical data types
# boolean,integer,unsigned integer,float,complex

# Boolean,Integer,unsigned integer,float,complex

# bool           true,false
# int8           Byte (-128 to 127)
# int16          Integer (-32768 to 32767)
# int32          Integer (-2147483648 to 2147483647)
# int64          Integer (-9223372036854775808 to 9223372036854775807)
# uint8          Unsigned integer (0 to 255)
# uint16         Unsigned integer (0 to 65535)
# uint32         Unsigned integer (0 to 4294967295)
# uint64         Unsigned integer (0 to 18446744073709551615)
# intp           Integer used for indexing, typically the same as ssize_t
# float32        float
# float64
# complex64         Complex number, represented by two 32-bit floats (real and imaginary components)
# complex128
# i - integer
# f - float
# ? - bool
# U - unicode


import numpy as np
a=np.array([True,False,True])
print(a)
print(a.dtype)

a=np.array([1+2j,3-6j])
print(a)
print(a.dtype)

arr=np.array(['apple','banana','cherry'])
print(arr)
print(arr.dtype)

a=np.array([8,2,3])
print(a)
print(a.dtype)

a=np.array([214783648,25435545,3])
print(a)
print(a.dtype)

a=np.array([214783648,25435545,3],dtype='i')
print(a)
print(a.dtype)

a=np.array([8,2,3],dtype='f')
print(a)
print(a.dtype)

a=np.array([-5,2,3],dtype='bool')
print(a)
print(a.dtype)

# unsigned
a=np.array([-5,2,3],dtype='uint8')
print(a)
print(a.dtype)

a=np.array([258,2,3],dtype='int8')
print(a)
print(a.dtype)

a=np.array([128,2,3],dtype='int8')
print(a)
print(a.dtype)

a=np.array([256,2,3],dtype='int8')
print(a)
print(a.dtype)

# unicode
arr=np.array(['apple','banana','cherry'],dtype='U')
print(arr)
print(arr.dtype)

