# Dataframe renaming
# used to relabel an axis

import pandas as pd
import numpy as np
df1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)
print("after renaming the rows and columns")
print(df1.rename(columns={'col1':'c1','col2':'c2'},
                 index={0:'apple',1:'banana',2:'durian'}))

