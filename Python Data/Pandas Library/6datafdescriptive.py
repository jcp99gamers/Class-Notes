# data frame descriptive statistics

# statistics are two:descriptive and inferential statistics
# inferential statistics are used when data is viewed as a subclass of a specific population
# descriptive statistic is summarise the data

# import pandas as pd
# d = {
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# df=pd.DataFrame(d)
# print(df)

# print(df.sum())   # default is axis=-,column wise
# print(df.sum(1))  # row wise

# to get avg value
# print(df.mean())

# variance:avg.square distance from mean
# standard deviation:sqr root of variance
"""ie,avg distance of points from mean value.
(if we know spread,we get an idea that how wide our points spread from
mean,is it is around mean or not.
numerical representation of spread is called sdt.dev"""

# to get the std deviation
# print(df.std())

# print(df.median())
# print(df.mode())  # most repeating number
# print(df.abs()) # +ve nums
# print(df.max())
# print(df.min())
# print(df.cumsum())   # adding each element to previous sum(cumulative sum)
# print(df.cumprod())
# print(df.count())



