
# representing data analysis in the form of graphs
# matplotlib is a python library used for 2D graphics

import matplotlib.pyplot as plt # pip install matplotlib
import pandas as pd
import numpy as np

# if only one sequence of data (it may be LIST or TUPLE)
# plt.plot([10,15,25,18])  # it consider as y value,x is index 0,1,2...
# plt.show()




############################
# if there are two sequence of data
# plt.plot([10,15,25,30],[2,4,6,8])   # it consider  x axis and y axis
# plt.show()

###########################
# providing labels
# plt.plot([10,15,25,30],[2,4,6,8])
# plt.ylabel("numbers")
# plt.xlabel("index")
# plt.title("myplot")
# plt.show()

#############################
# adding style
# x1=[10,15,25,30]
# y1=[2,4,6,8]
# x2=[15,17,25,32]
# y2=[2,5,7,10]
# x3=[10,20,30,40]
# y3=[4,3,6,12]
# plt.plot(x1,y1,'g',label='Line one',Linewidth='3')
# plt.plot(x2,y2,'r',label='Line two',Linewidth='5')
# plt.plot(x3,y3,'y--',label='Line one',Linewidth='5')
# plt.plot(x3,y2,'bo',label='Line one',Linewidth='5')
# plt.plot(x3,y1,'ks',label='Line one',Linewidth='5')

# plt.ylabel("numbers")
# plt.xlabel("index")
# plt.title("myplot")
# plt.grid()   # adding grids
# plt.legend()  # used to show label in the graph
# plt.show()

############################
# using data frame
# df=pd.DataFrame({
#     'pig':[20,18,489,675,1776],
#     'horse':[4,25,281,600,1900]
#     },index=[1990,1997,2003,2009,2014])

# print(df)
# df.plot.line()
# df.plot.line(subplots=True)  # seperate the graph
# plt.savefig("file.png")  # to save the plot
# plt.show()



# the subplots() function takes three arguments that describes
# the layout of the figure.## The layout is organized in rows
# and columns, which are represented by the first and second argument.
# The third argument represents the index of the current plot

df=pd.DataFrame({
    'pig':[20,18,489,675,1776],
    'horse':[4,25,281,600,1900],
    'x':[5,30,51,100,200]},
    index=[1990,1997,2003,2009,2014])
print(df)
# we can specify each subplot
# plt.subplot(3,1,1)  # no of plots,below/side,which plot[nrows,ncolumns,plotno]
# plt.plot(df.pig,df.horse,'y--')
# plt.subplot(3,1,2)  # no of plots,below/side,which plot
# plt.plot(df.pig,df.x,'gd')
# plt.subplot(3,1,3)
# plt.plot(df.horse,df.x,'rs')
# plt.show()

# plot by side by side
plt.subplot(2,2,1)
plt.plot(df.pig,df.horse,'y--')
plt.subplot(2,2,2)  # no of plots,below/side,which plot
plt.plot(df.pig,df.x,'gd')
plt.show()

##################################

