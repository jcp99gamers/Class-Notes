# 7Example_Lungs_Case_Study.py
import pandas as pd

df = pd.read_csv("C:\\Users\\best\\Downloads\\lung.csv")
print(df)
print(df.shape)
print(df.columns)

"""
inst:	Institution code
time:	Survival time in days
status:	censoring status 1=censored, 2=dead
age:	Age in years
sex:	Male=1 Female=2
ph.ecog:	ECOG performance score (0=good 5=dead)
ph.karno:	Karnofsky performance score (bad=0-good=100) rated by physician
pat.karno:	Karnofsky performance score as rated by patient
meal.cal:	Calories consumed at meals
wt.loss:	Weight loss in last six months
"""

# print(df.dtypes)  # to get datatype of all columns
# df.set_index("Unnamed: 0", inplace=True)
# print(df.head())
# print(df.sex)


# resetting values 1 & 2 in column "sex"
# df.loc[df.sex==1,"sex"]="Male"
# df.loc[df.sex==2,"sex"]="Female"
# print(df.sex)

# removing selective items from a column
# creating selected indexes to a list
# l=df.loc[df.status==1].index.tolist()
# print(l)
# df=df.drop(l)  # deleting rows with list
# print(df.status)