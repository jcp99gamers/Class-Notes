import pandas as pd
import matplotlib.pyplot as plt

# A bar chart or bar graph is a chart or graph that presents categorical data
# with rectangular bars with heights or lengths proportional to the values that
# they represent. The bars can be plotted vertically or horizontally.

# BAR graph-plots vertical rectangles with constant width
# BARH graph-plots horizontal rectangles withconstant heights


# bar plots used mainly for compare two groups
# bar plots are useful if the changes are larger

# plt.bar([1,3,5,7,9],[5,2,7,8,2])  # x,y
# plt.show()

# plt.barh([1,3,5,7,9],[5,2,7,8,2])  # x,y
# plt.show()

# x=[1,3,5,7,9]
# y=[5,2,7,8,2]
# plt.bar(x,y,label="example")  # x,y
# plt.legend()
# plt.xticks(x,["g1","g2","g3","g4","g5"])
# plt.xlabel("bar number")
# plt.ylabel("bar height")
# plt.title("bar graph")
# plt.show()

#######################
df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
   'num_pets':[5,1,0,5,2,2,3]
})
print(df)
# bar plot for single column /field
df['age'].plot.bar()
plt.show()

# bar plot by two column /field
df.plot.bar(x='age',y='num_pets')
plt.show()

# if we want to change label
df.plot.bar(x='age',y='num_pets',label="NumOfPets")
plt.xlabel("age")
plt.ylabel("num_pets")
plt.show()

# if we want to change x label and y label
df.plot.bar(x='age',y='num_pets',label="NumOfPets",xlabel='age',ylabel='pets',title="age vs numofpets")
plt.show()

# to change the color
# df.plot.bar(x='age',y='num_pets',label="NumOfPets",xlabel='age',ylabel='pets',\
#             title="age vs numofpets",color='orange')
# plt.show()

# plt.bar(df.age,df.num_pets,label="NumOfPets",color="orange",width=3)
# plt.legend()
# plt.title("age vs pets")
# plt.xlabel("age")
# plt.ylabel("pets")
# plt.show()