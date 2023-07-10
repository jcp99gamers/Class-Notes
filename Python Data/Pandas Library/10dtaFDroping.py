# dataframe droping

import pandas as pd
import numpy as np
dframe = pd.DataFrame(np.arange(16).reshape((4,4)), index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
print(dframe)
print(dframe.drop(['red']))
print(dframe.drop(['red','blue']))

# for columns,
df=dframe.drop(['pen','pencil'],axis=1)
print(df)