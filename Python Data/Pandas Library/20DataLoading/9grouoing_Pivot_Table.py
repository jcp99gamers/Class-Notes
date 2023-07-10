"""pivot table is used to summarize and
aggregate data inside data frame"""

import pandas as pd
import numpy as np

data=pd.read_excel("C:\\Users\\best\\Downloads\\SaleData.xlsx")
print(data)
# print(data.dtypes)
# print(data.shape)
print(data.columns)
# print(data.describe())
# print(data.nunique())

# group by region and manager
# print(pd.pivot_table(data,index=["Region","Manager"]))

# group by a condition
# print(data.query('Region==["West"]'))
# print(data.query('Manager==["Timothy"]'))
# df=pd.pivot_table(data,index=["Region","Manager"])
# print(df)
# print(df.keys())
# print(df.columns)
# print(df.index)
# print(df.values)

# to specify a column by values (only we get sale amt column)
print(pd.pivot_table(data,index=["Region","Manager","SalesMan"],values="Sale_amt"))

# can use aggregate fn using aggfunc(mean,sum,std..)
print(pd.pivot_table(data,index=["Region"],aggfunc="mean"))


# find unit price of each salesman and their managers and region
# print(pd.pivot_table(data,index=["Region","Manager","SalesMan"],values="Unit_price"))


# find item wise unit sold (average value)
# print(pd.pivot_table(data,index=["Item"],values="Units",aggfunc="mean"))
# print(pd.pivot_table(data,index=["Item"],values="Units"))

# find item wise unit sold(item wise total number)
# print(pd.pivot_table(data,index=["Item"],values="Units",aggfunc="sum"))

# find region wise total sale amount
# print(pd.pivot_table(data,index=["Region"],values="Sale_amt",aggfunc="sum"))

# region and item wise  total sale
# print(pd.pivot_table(data,index=["Region","Item"],values="Sale_amt",aggfunc="sum"))

# count manager wise sale orders and total sale amount for each manager
# print(pd.pivot_table(data,index=["Manager"],values="Sale_amt",aggfunc=["sum",len()]))
# print(pd.pivot_table(data,index=["Manager"],values="Sale_amt",aggfunc=[np.sum,len()]))

# find total sale of each sales man and manager and print actual total amount of all sales at bottom
# print(pd.pivot_table(data,index=["Manager","SalesMan"],values="Sale_amt",aggfunc=[np.sum],margins=True))

# find total sale amount region wise ,manager wise, salesman wise
# result=pd.pivot_table(data,index=["Region","Manager","SalesMan"],values="Sale_amt",aggfunc=[np.sum])
# print(result)

# from the result find the sale amt if the manager is "dounglas"
# result=pd.pivot_table(data,index=["Region","Manager","SalesMan"],values="Sale_amt",aggfunc=[np.sum])
# print(result.query('Manager==["dounglas"]'))
# print(data.query('Manager==["dounglas"]'))

# find region wise no of television and home theatres sold
# result=pd.pivot_table(data,index=["Region","Item"],values="Units",aggfunc=[np.sum])
# print(result)
# print(result.query('Item==["Television"] | Item==["Home Theater"]'))
# print(result.query('Item==["Television","Home Theater"]'))
# print(result.query('Item in ["Television","Home Theater"]'))

# fond the max and min sale amount of items
# print(pd.pivot_table(data,index=["Item"],values="Sale_amt",aggfunc=["max","min"]))
































# Q Find item wise unit sold , ( item wise total number)
print(pd.pivot_table(data,index=["Item"],values="Units",aggfunc="sum"))

# Q Find region wise total sale amount
print(pd.pivot_table(data,index=["Region"],values="Sale_amt",aggfunc="sum"))

# Q region wise & item wise total sale
print(pd.pivot_table(data,index=["Region","Item"],values="Sale_amt",aggfunc="sum"))

# Q count manager wise sale orders and mean value of sale amount
print(pd.pivot_table(data,index=["Manager"],values=["Sale_amt","Units"],aggfunc=["mean","sum"]))

# Q Find  total sale amount region wise,manager wise,sales man wise
print(pd.pivot_table(data,index=["Region","Manager","SalesMan"],values="Sale_amt",aggfunc="sum"))

# Find total sale  of each salesman and manager and print actual total amount of all sales at bottom.
print(pd.pivot_table(data,index=["Manager","SalesMan"],values="Sale_amt"))

# Find  total sale amount region wise,manager wise,sales man wise
result=pd.pivot_table(data,index=["Region","Manager","SalesMan"],values="Sale_amt",aggfunc="sum")

# From the result find the sale amt if the  manager is "Dounglas"
print(result.query('Manager==["Douglas"]'))
print(data.query('Manager==["Douglas"]'))

# find region wise no of 'Televisions' and 'Home Theatres' sold
result=pd.pivot_table(data,index=["Region","Item"],values="Units",aggfunc=[np.sum])
print(result)
print(result.query('Item==["Television","Home Theatre"]'))

# find the max and min sale ant of the items
print(pd.pivot_table(data,index=["Item"],values="Sale_amt",aggfunc=["max","min"]))





