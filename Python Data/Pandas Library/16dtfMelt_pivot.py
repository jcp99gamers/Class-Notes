import pandas as pd
'''
Melting:melt in pandas reshape data frame from wide format to long format
'''

# it reduces the columns and increases the rows


df = pd.DataFrame(data = {
   'Day' : ['MON', 'TUE', 'WED', 'THU', 'FRI'],
   'Google' : [1129,1132,1134,1152,1152],
   'Apple' : [191,192,190,190,188],
   'Amazone' : [210,524,430,325,551]
})
print(df)
# here we can use "day"  as a variable/identifier because it is common to other fields
# so on day basis we can do reshape
# that we want to mention as "id_vars['col_names']"

df1=df.melt(id_vars=['Day'])
print(df1)
df1=pd.melt(df,id_vars=['Day'])
print(df1)
'''this generate 2 columns,
variable-it contains actual column names
value-it contains actual values'''
# to rename that columns use:
'''
var_name=['column_name for variable']
value_name=['column_name for value']
'''

# df1=df.melt(id_vars =['Day'],var_name="company",value_name="sales")
# print(df1)


# value_vars:from the result if we need only specific variables values
# df1=df.melt(id_vars =['Day'],value_vars=['Google','Amazone'],var_name="company",value_name="sales")
# print(df1)

'''
pivot: reverse melt(opposite concept of melting)
'''
# index-what we need as rows
# columns-what we need as columns


# originaldata=df1.pivot(index='Day',columns="company")["sales"].reset_index()
# originaldata.columns.name=None
# print(originaldata)