
import pandas as pd
import numpy as np

data = pd.read_json("C:\\Users\\best\Downloads\\XML, JSON Viewer.JSON")
print(type(data))
print(data)
#
df =pd.DataFramedf = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                    ('bird', 'Psittaciformes', 24.0),
                    ('mammal', 'Carnivora', 80.2),
                    ('mammal', 'Primates', np.nan),
                    ('mammal', 'Carnivora', 58)],
        index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
        columns=('class', 'order', 'max_speed'))
print(df)
df.to_json("file.JSON")
data =pd.read_json("file.JSON")
print(data)

#########