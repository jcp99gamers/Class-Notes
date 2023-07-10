import pandas as pd
df=pd.DataFrame({"specious":["A","B","C"],"days":[10,12,13],
                 "time":["10/09/2010 2:30:0","12/09/2010 4:30:0","09/09/2010 5:30:0"]})



print(df)
print(type(df.time[0]))    # data is str format
df["time"]=pd.to_datetime(df.time) # converting to time stamp
print(type(df.time[0]))
print(df)

# to get year only from that column dt.year
print(df.time.dt.year)
print(df.time.dt.weekday)
print(df.time.dt.day_name())
print(df.time.dt.month)