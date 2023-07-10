# pandas provides a set of string functions which make it easy to operate on string data
# most  importantly,it not consider nan values

import pandas as pd
import numpy as np
# for series

# s=pd.Series(['Tom','William Rick','John','Albert@alb',np.nan,'1234',' SteveSmith'])
# print(s)
# print(s.str.lower())
# print(s.str.upper())
# print(s.str.len())
# print(s.str.strip())
# print(s.str.len())
# s1=s.str.strip()
# print(s1.str.len())
# print(s.str.cat(sep='/'))   # to join using seperator

"""
we have label encoding and one hot encoding for string
in label encoding we gives 1,2,3,... for unique string
(in label encoding,machine may find out any relation b/w digits,like 1+2=3,1<3,etc....so we follows OHE)
on OHE we follows binary numbers
(it forms a vector,its length=no of unique strins)
# if the no of categories increases,vector became sparse

designation     teacher   student  officestaff
teacher          1         0        0
teacher          1         0        0
student          0         1        0
student          0         1        0
student          0         1        0
office staff     0         0        1
office staff     0         0        1
"""
# print(s.str.get_dummies())
# print(pd.get_dummies(s))

# print(s.str.contains(' '))    # to check whitespace
# print(s.str.replace('@','$'))
# print(s.str.repeat(2))
# print(s.str.count('m'))
# print(s.str.startswith('T'))
# print(s.str.endswith('T'))
# print(s.str.find('e'))   # -1 if not matching
# print(s.str.findall('e'))
# print(s.str.swapcase())
# print(s.str.isupper())
# print(s.str.islower())
# print(s.str.isnumeric())


#################
# for data frame

# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#      'Sex':pd.Series(['male','female','male','male','male','male','female']),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# df=pd.DataFrame(d)
# print(df)
# print(df['Name'].str.lower())
# print(df['Name'].str.len())
# print(df['Name'].str.get_dummies())
# print(pd.get_dummies(df))
# df['Name']=df['Name'].str.lower()
# print(df)
# df.set_index('Name',inplace=True)
# print(df)

