import pandas as pd
import matplotlib.pyplot as plt

'''histogram : we have quantitative variables.eg:how much each age group contributing towards GDP growth
bar plots :if we have categorical varuables .eg:GDP growth of every city in a country
'''

# df=pd.DataFrame({'length':[1.5,0.5,1.2,0.9,3],'width':[0.7,0.2,0.15,0.2,1.1]},index=['pig','rabbit', 'duck', 'chicken', 'horse'])
# print(df)
# # hist=df.hist(bins=2)
# df.hist(bins=3)
# plt.show()

#####################
# population_ages=[22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
# plt.hist(population_ages)
# plt.xlabel("x")
# plt.ylabel("count")
# plt.title("Histogram")
# plt.legend()
# plt.show()

# bins:to set the x axis range
# rwidth:to set the width

population_ages=[22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120]
plt.hist(population_ages,bins,rwidth=0.8,edgecolor='black')
plt.xlabel("x")
plt.ylabel("count")
plt.title("Histogram")
# plt.legend()
plt.show()

