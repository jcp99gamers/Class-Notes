import pandas as pd
import numpy as np

# df=pd.DataFrame([[1,2,3],[np.nan,2,5],[5,7,10],[4,8,3],[5,np.nan,6]],columns=['c1','c2','c3'])
# print(df)
# print(df.isna())   # to check whether nan value present

# print(df.loc[4,:])
# print(df.loc[4,:].isna())     # to check particular row
# dfnew=df.dropna()  # to drop row with value nan/new data frame
# print(dfnew)

# dfnew=df.fillna(10)   # to fill nan position /new data frame
# print(dfnew)

# dfnew=df.bfill()  # to fill with below value
# print(dfnew)

# dfnew=df.ffill()   # to fill with upper value
# print(dfnew)
# print(df.interpolate())  # to fill nan with any random value


# to change '2' in the df with nan
# dfnew=df.replace(2,np.nan)
# print(dfnew)


# change '5' in the c1 column with nan
# dfnew=df['c1'].replace(5,np.nan)
# print(dfnew)
# or
# df.loc[df.c1==5,'c1']=np.nan
# print(df)


# change nan value in c2 column with avg of c2
### dfnew=df['c2'].replace(np.nan,df['c2'].mean())
### print(dfnew)

# d=df.c2.fillna(df.c2.mean())
# print(d)



