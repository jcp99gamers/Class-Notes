# A boxplot is a standardized way of displaying the distribution of data based on
# a five number summary (“minimum”, first quartile (Q1), median, third quartile (Q3),
# and “maximum”).


import pandas as pd
import matplotlib.pyplot as plt

# df=pd.read_csv("C:/Users/best/Downloads/mtcars.csv")
# print(df)
# print(df.cyl.unique())

# a=df[df.cyl==4]
# print(a)
# print(a.describe())

# df.boxplot(by="cyl",column="mpg")
# plt.show()

# An outlier is an observation that is numerically distant from the rest of the data.
# When reviewing a box plot, an outlier is defined as a data point that is located outside
# the whiskers of the box plot.
#
# outside 1.5 times the inter quartile range above the upper quartile and below the
# lower quartile (Q1 - 1.5 * IQR or Q3 + 1.5 * IQR).


'''seaborn: is a library for making statistical graphs
in python on top of matplotlib
'''

import seaborn as sns


# x1=[10,15,25,30]
# y1=[2,4,6,8]

# line graph
# sns.lineplot(x=x1,y=y1)
# plt.show()

# bar graph
# sns.barplot([1,3,5,7,9],[5,2,7,8,2])
# plt.show()

# scatterplot
df=pd.DataFrame([[5.1,3.5,0],[4.9,3.0,0],[7.0,3.2,1],
                 [6.4,3.2,1],[5.9,3.0,2]],
                columns=['length','width','species'])
# print(df)
# sns.scatterplot(x='length',y='width',hue='species',data=df)
# plt.show()

# specific color=palette
# sns.scatterplot(x='length',y='width',hue='species',data=df,
#                 palette=['green','orange','brown'])
# plt.show()

# histogram
# population_ages=[22,55,62,45,21,22,34,42,42,4,99,102,
#                  110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
# bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# sns.histplot(data=population_ages,bins=bins)
# plt.show()

# density histogram
# sns.displot(population_ages,bins=bins)
# plt.show()

# sns.displot(population_ages,bins=bins,kde=False)
# plt.show()


# boxplot
# df=pd.read_csv("C:/Users/best/Downloads/mtcars.csv")
# sns.boxplot(x="cyl",y="mpg",data=df)
# plt.show()