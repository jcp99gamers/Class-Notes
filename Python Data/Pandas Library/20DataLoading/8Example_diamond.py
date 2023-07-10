import pandas as pd

# github is a hosting platform for public and private software codes
# data=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
data=pd.read_csv("C:\\Users\\best\\Downloads\\data.csv")
# print(data)
# print(data.shape)
# print(data.head())
# print(data.describe())
# print(data.nunique())
# print(data.color[0])
# print(data.dtypes)

# create a column "quality_color" by join "cut" column and "color"
# then remove cut and color from df
# data["quality_color"]=data.cut+"_"+data.color
# print(data.head())
# data.pop("cut")
# data.pop("color")
# print(data.head())
# print(data)

# print(data.columns)
# df=data.reindex(columns=['carat','quality_color','clarity','depth','table','price','x','y','z'])
# print(df.head())