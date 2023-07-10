# dataframe creation

# used for heterogeneous data
# size is mutable
# data also mutable
# it have labeled axis
# can load data from diff format


import pandas as pd
# 1.using list

# df1=pd.DataFrame([10,20,30])
# print(df1)

# df2=pd.DataFrame([10,20,30],['a','b','c'])  # custom index
# print(df2)

# df3=pd.DataFrame([[10,20,30],[40,50,60]])
# print(df3)

# df4=pd.DataFrame([[10,20,30],[40,50,60]],['a','b'])  # custom index
# print(df4)

# df5=pd.DataFrame([[10,20,30],[40,50,60]],['a','b'],columns=['id','age','mark'])
# print(df5)

# df5.set_index('id',inplace=True)
# print(df5)

# df6=pd.DataFrame([[1,"ajith",3],[2,"alex",6]],columns=["ID","NAME","MARK"])
# print(df6)

#####################################
# 2.using dictionary

# d={'pid':[1,2,4],'name':['book','pen','pencil'],'price':[20,10,5]}
# df=pd.DataFrame(d)
# print(df)

# df.set_index('pid',inplace=True)
# print(df)

# DataF=pd.DataFrame(d,index=['p1','p2','p3'])
# print(DataF)

# if give a list of dict,it will group it by key
# if there is no value,it fill with nan

# l=[{'a':'Ann','b':'Tom'},
#    {'c':'Anna','a':'Kevin'}]
# df=pd.DataFrame(l)
# print(df)

# if give a dict of series,
# data={'one':pd.Series([1, 2, 3])}
# d=pd.DataFrame(data)
# print(d)