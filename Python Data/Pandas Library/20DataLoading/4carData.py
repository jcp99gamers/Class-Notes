import pandas as pd
df=pd.read_csv("C:/Users/best/Downloads/mtcars.csv")
# [, 1]	mpg	Miles/(US) gallon
# [, 2]	cyl	Number of cylinders
# [, 3]	disp	Displacement (cu.in.)
# [, 4]	hp	Gross horsepower
# [, 5]	drat	Rear axle ratio
# [, 6]	wt	Weight (1000 lbs)
# [, 7]	qsec	1/4 mile time
# [, 8]	vs	Engine (0 = V-shaped, 1 = straight)
# [, 9]	am	Transmission (0 = automatic, 1 = manual)
# [,10]	gear	Number of forward gears
# [,11]	carb	Number of carburetors
print(df)
# print(df.columns)

# df.set_index("Unnamed: 0",inplace=True)
# print(df)



# print car details if millage b/w 15 and 20

# print((df.mpg > 15)&(df.mpg <20))
# print(df[(df.mpg > 15)&(df.mpg <20)])
# print(df.loc[(df.mpg > 15)&(df.mpg <20)])
# print(df.loc[(df.mpg >= 15)&(df.mpg <20),"mpg"])


# print manual type car details with 6 cylinder engine
# print(df[(df.cyl==6)&(df.am!=0)])


# change automatic car parameter from "0" to "2" in the same df
# df.loc[df.am==0,"am"]=2
# print(df.am)
# print(df['am'].replace(0,2))  # it will not change df
# print(df)


# adding 2 to every data in vs column
# df['vs']=df['vs']+2
# print(df)
# df.loc[:,"vs"]+=2
# print(df.vs)


# delete rows and columns "am" where value is 1

# l=df.loc[df.am==1].index.tolist()
# print(l)
# df=df.drop(l)  # deleting rows with list
# print(df.am)
# print(df)

# insert a column into a position
import numpy as np
a=np.random.rand(32)
print(a)

df.insert(2,"example",a)  # insert column into dataframe at specified location
print(df)

df["new"]=10
print(df)