import pandas as pd
import numpy as np

df1=pd.DataFrame(np.array([1,2,3,4]).reshape(2,2),index=[1,2],columns=[1,2])
df2=pd.DataFrame(np.array([7,8,5,6]).reshape(2,2),index=[1,2],columns=[1,2])

print(df1)
print(df2)
print(df1+df2)
print("sum is :",df1.add(df2))


# if the index changes matching indexes get added and remaining nan
df3=pd.DataFrame(np.array([7,8,5,6]).reshape(2,2),index=[1,3],columns=[1,2])
print(df3)
print(df1+df3)