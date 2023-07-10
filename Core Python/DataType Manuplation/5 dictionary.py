# can't index(unorderd collection)
# mutable
#empty dict
s={}
# print(type(s))
# s=dict()
# print(type(s))
# print(s)
##########
q={"a":5,"b":1,55:"c"}
# print(q)
# w=dict([("a",8),("b",3)])     #also we can use list of tuples
# print(w)
##########
# print(q["a"])
# print(q[55])
# print(q.get("a"))
# print(q.get(55))
############
# q={"a":5,"b":1,55:"c"}
# print(q)
# q["x"]=45 #create new pair of value
# print(q)
# q["a"]="boy"   #it will change the existing value
# print(q)
#############
#remove and return
q={"a":5,"b":1,55:"c"}
print(q)
r=q.pop("b")
print(r)
print(q)
q.popitem() # #to remove any key
print(q)
####
# del q
# print(q)
# q.clear()
# print(q)


# del q["a"]
# print(q)
###########
# b=q.copy()
#########


#programe to change city to location
sampledict={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"new york"
}
sampledict["location"]="new york"
print(sampledict)
# sampledict.pop("city")
# print(sampledict)
#########
#create dictionary using fromkeys
# s={}.fromkeys(["maths","chem","eng"],0)
# print(s)
# s={}.fromkeys(("maths","chem","eng"),0)
# print(s)
# s={}.fromkeys(["maths"],0)
# print(s)
s={}.fromkeys("maths",0)
print(s)
########
#.items
# s={"a":10,"b":20,"c":30}
# print(s.items())  #it shows list of tuples
# a=s.items()
# print(type(a))
# ##
#.keys
# print(s.keys())  #it shows the keys in dictionary
##
#.values
# print(s.values())  #it shows the values in the dictionary
#########
#update method
# s.update({"ann":"cs","akhil":"mech"})
# print(s)
# ###########
# print(dir(s))
# methods and attributes using to describe dictionary
#########
#for iterating tuples
# d={"a":10,"b":50,"c":40}
# for item in d.items():
#     print(item)
# ##
# #for iterating values
# for item in d.values():
#     print(item)
#
# for item in d:
#     print(item)
# ##
# #for itwrating keys
# for item in d.keys():
#     print(item)
# ##
# for k,v in d.items():
#     print(k)
#     print(v)
##########

# finding the sum of marks
# d={"maths":10,"chemistry":50,"english":40}
# sum=0
# for item in d.values():
#     sum=sum+item
# print(sum)
######
#find maximum value
# d={"maths":10,"chemistry":50,"english":40}
# max=0
# for item in d.values():
#     # print(item)
#     if max<item:
#         max=item
# print(max)
#########
# find the key value pair if the value is >2
# d={"a":1,"b":5,"c":3}
# new={}
# for k,v in d.items():
#     if v>=2:
#         new.update({k:v})
# print(new)
########

#############
# d={"a":10,"b":100,"a":200}
# print(d)
#nested dictionray
# d={101:{"name":"ram","mark":100},
#    102:{"name":"bibin","mark":99}}
# print(d)
# print(d[101])
# print(d[101]["name"])
# print(d[101]["mark"])
##########

#change varshas salary to 70000

sampleDict = {
     'emp1': {'name': 'John', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Varsha', 'salary': 6500}
}

# sampleDict['emp3']['salary']=70000
# print(sampleDict)
# or #

# for k,v in sampleDict.items():
#     for k1,v1 in v.items():
#         print(v1)
#         if v1=='Varsha':
#                 sampleDict[k]['salary'] = 70000
# print(sampleDict)
###########
# find the min value
# sampleDict={
#     'physics':82,
#     'math':65,
#     'history':75
# }
# print(sampleDict.values())
# l=sampleDict.values()
# print(type(l))
# print(min(l))
# print(max(l))
# print(sum(l))
##########


# create a dictionary using below data and find the total mark
# studentData:
# 111:    name:TOM
#         email: tom@gmail.com
#         sem: sem1: sub1:2,sub2:5,sub3:8
#              sem2 :sub1:7,sub2:6
# 222:    name:RAMU
#         email: ramu@gmail.com
#         sem: sem1: sub1:8,sub2:2,sub3:9
#              sem2 :sub1:7,sub2:6


StudentData ={
"111" :{
      "name" :"TOM",
      "email" :"tom@gmail.com",
      "sem" :{"sem1": {"sub1":2,"sub2":5,"sub3":8},
             "sem2" :{"sub1":7,"sub2":6 }}
       } ,
"222"  : {
      "name":"RAMU",
      "email": "ramu@gmail.com",
      "sem": {"sem1": {"sub1":8,"sub2":2,"sub3":9},
             "sem2" :{"sub1":7,"sub2":6}
              }
         }
}
# program to calculate total mark of student

# studentinfo= {
#    "name" : "anil",
#    "email" : "anil@ddd.com",
#    "marks" : {"sem1" : 100, "sem2" : 200,"sem3" : 300}
# }
# sum= 0
# for k,v in studentinfo.items():
#     print(k,v)
#     if k == 'marks':
#           for k1,v1 in v.items():
#             # print(v1)
#             sum+=v1
# print(studentinfo['name'],":",sum)
############



















# create dictionary keys="kc" and values "v**2"
# d={"a":1,"b":5,"c":0,"d":3}
# ### new={}
# s="c"
# d={"a":1,"b":5,"c":0,"d":3}
# for i,m in d.items():
#     i=i+s
#     m=m**2
#     new.update({i:m})
# print(new)###
#or#
# new={k+'c':v**2 for k,v in d.items() }
# print(new)
########################
# print id,name mail id,total mark of both students

# data = {
#    "100" : {
#        "name" : "anil",
#        "email" : "anil@ddd.com",
#        "marks" : {"sem1" : 100,"sem2" : 200,"sem3" : 300}
#             },
#    "101" :{
#        "name" : "binil",
#        "email" : "binil@ddd.com",
#        "marks" : {"sem1" : 200,"sem2" : 200,"sem3" : 300}
#             }
# }
#
# for id,info in data.items():
#     total_mark=0
#     for k,v in info.items():
#         if k=='marks':
#             for sem,mark in v.items():
#                 total_mark+=mark
#     print(id,info['name'],info['email'],total_mark)
#######################


# create a dictionary using below data and find the total mark
# studentData:
# 111:    name:TOM
#         email: tom@gmail.com
#         sem: sem1: sub1:2,sub2:5,sub3:8
#              sem2 :sub1:7,sub2:6
# 222:    name:RAMU
#         email: ramu@gmail.com
#         sem: sem1: sub1:8,sub2:2,sub3:9
#              sem2 :sub1:7,sub2:6


# StudentData ={
# "111" :{
#       "name" :"TOM",
#       "email" :"tom@gmail.com",
#       "sem" :{"sem1": {"sub1":2,"sub2":5,"sub3":8},
#              "sem2" :{"sub1":7,"sub2":6 }}
#        } ,
# "222"  : {
#       "name":"RAMU",
#       "email": "ramu@gmail.com",
#       "sem": {"sem1": {"sub1":8,"sub2":2,"sub3":9},
#              "sem2" :{"sub1":7,"sub2":6}
#               }
#          }
# }



# print(StudentData)
# for id,info in StudentData.items():
#      totalmark=0
#      for k,v in info.items():
#          if k=='sem':
#              for k1,v1 in v.items():
#                  for k2,v2 in v1.items():
#                      totalmark=totalmark+v2
# print(totalmark)
################