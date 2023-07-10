# https://www.w3schools.com/python/python_regex.asp

# regular expression in python
# it is a sequence of characters used for pattern matching
# ie,whether the pattern is available in the sequence of characters or string
# pattern is a character or a group of character
# or we can say when ever we i/p an information,how we can extract a required information
# processing the i/p information and getting required info in many ways

# to implement regular expression we have a module "re"
# it is a collection of predefined fns to process/validate i/p text
# functions
# match() :it is used to test the i/p string starts with a specific pattern or not
# search() :to test a specified pattern is present or not in string.it return a match object
#          :we have diff methods to display the result
#          :start()-starting position of occurrence
#          :end()-ending pos.
#          :span()-tuple of start and end pos
#          :string()-actual string
# findall() :to find duplicates of specified pattern in the string (how many times as a list).else empty list

###################################
# match()
# it is used to test the i/p string starts with a specific pattern or not
# on success,it return the match object with its position
# on failure,it return none

import re
line="python is an object oriented programing language"
print(line)
r1=re.match('hi',line)
print(r1)
#
# r1=re.match('is',line)
# print(r1)
# it will not consider new lines
# import re
# line="python is an object oriented programing language \nPython is interpreted"
# print(line)
# r1=re.match('python',line)
# print(r1)
# if the match found,we can use any condition
# if r1:
#     print("yes we got a match from string")
# else:
#     print("nothing found")

################################
# findall()
# to find duplicates of specified pattern in the string (how many times as a list).else empty list

# import re
# line="python is an object oriented programing language \npython is interpreted"
# x=re.findall("pyth",line)
# print(x)

# import re
# line="python is an object oriented programing language \nPython is interpreted"
# x=re.findall("o",line)
# print(x)

# import re
# line="python is an object oriented programing language \nPython is interpreted"
# x=re.findall("xyz",line)
# print(x)

#################################
# search(): to test a specified pattern is present or not in string
#         :we have diff methods to display the result
#         :start()-starting position of occurance
#         :end()-ending pos.
#         :span()-tuple of start and end pos

# it return a match object.else none
# it shows only first instance
# it searches anywhere in string
# it can search new line

# import re
# line="python is an object oriented programing language \nPython is interpreted"
# x=re.search("pyth",line)    # return match object
# print(x)


# import re
# line="python is an object oriented programing language \nPython is interpreted"
# x=re.search("pyth",line).start()
# print(x)

# import re
# line="python is an object oriented programing language \nPython is interpreted"
# x=re.search("pyth",line).end()
# print(x)


# import re
# line="python is an object oriented programing language \nPython is interpreted"
# x=re.search("pyth",line).span()
# print(x)


# import re
# line="python is an object oriented programing language \nPython is interpreted"
# x=re.search("pyth",line).group()     #to get match string
# print(x)
#####################################

# split()
# how we can split a string using an expression.return a list

# import re
# line="python is an object oriented programing language"
# x=re.split(" ",line)
# print(x)

# import re
# line="python is an object oriented programing language"
# x=re.split("p",line)
# print(x)

# import re
# line="python is an object oriented programing language"
# x=re.split(" ",line,2)     # 3rd is max split(max.split required)
# print(x)

###################################
# sub

# import re
# line="python is an object oriented programing language"
# x=re.sub("p","X",line)
# print(x)
#
# import re
# line="python is an object oriented programing language"
# x=re.sub("p","X",line,1)
# print(x)


###############################
# metacharacters and special sequences
# these are also used in above fns for pattern matching

# metacharacters

# ^   -cap symbol used for startswith
# $   - symbol used for endswith

# *   - 0 or more occurrences of a pattern
# +   - 1 or more occurrences of a pattern
# ?   - 0 or ONE occurrences of a pattern
# {n}  - strictly n times of occurrence
# {n,m}  - limit: min-n times & max. m times can  occr
# {,m}  - 0 to max. up to m times
# {n,}  - at least n times or more

# special sequences
# \w  - a-z,A-Z,0-9,_   it represents
# \W  - non chara. and digits (ie for special sybls)it represents
# \d  - 0-9   it represents
# \D  - non digit   it represents
# \s  - white space   it represents
# \S  - non white space chara.   it represents
# .   - any chara. except new line

# []-it return a match if string contain a character /pattern specified in the []
#     -it used to represent a group of characters
# [abc]-any one of these chara
# [a-z]-any chara in this range
# [0-9][0-9]-we can use combination also,here we means two digit number

##################################
import re

# regex='^a...n$'
# result=re.match(regex,"alaan")
# print(result)

# regex='^a....'
# result=re.match(regex,"alaan")
# print(result)

# regex='^(al)...'
# result=re.match(regex,"alaan")
# print(result)

# regex='^(al)...'
# result=re.match(regex,"fgalaan")
# print(result)

# regex='^....n$'
# result=re.match(regex,"alaan")
# print(result)

# regex='^a\w\w\wn$'
# result=re.match(regex,"alaan")
# print(result)

# regex='^a\w+n$'
# result=re.match(regex,"alaan")
# print(result)


# regex='a[a-z]n$'
# result=re.match(regex,"alaan")
# print(result)

# regex='a[a-z]+n$'
# result=re.match(regex,"alaan")
# print(result)

# regex='a[a-z][a-z][a-z]n$'
# result=re.match(regex,"alaan")
# print(result)

# regex='\w+'
# result=re.match(regex,"alaan")
# print(result)

# regex='\w\w'
# result=re.match(regex,"alaan")
# print(result)

# regex='\w\w'
# result=re.search(regex,"alaan")
# print(result)

# regex='\w\w'
# result=re.findall(regex,"alaan")
# print(result)

# regex='\w+'
# result=re.search(regex,"alaan")
# print(result)
# if result:
#     print("result obtained")

# regex='\w{3}'
# result=re.search(regex,"aaaaa")
# print(result)

# regex='\w{2}'
# result=re.findall(regex,"aaaaa")
# print(result)

# regex='\S'   # every chara other than white space
# result=re.findall(regex,"akjf lknfv")
# print(result)

# regex='\S+'          # every one or more chara other than white space,ie,each word in the string
# result=re.findall(regex,"akjf lknfv")
# print(result)

##  [A-Z]  : anything from A to Z
# s="Hello, There,How"
# result=re.findall('[A-Z]',s)
# print(result)

# s="Hello, There,How"
# result=re.findall('[A-Z,]',s)     # find all either it is A-Z or ,
# print(result)

# s="HELLO, There,How"
# result=re.findall('[A-Z]+',s)   # one or more A-Z
# print(result)


# s="HELLO, There,How"
# result=re.findall('[A-Z]*',s)
# print(result)

# full string
# s="HELLO, There,How"
# result=re.findall('[a-zA-Z]+',s)    # order is not important
# print(result)

# s="Hello, There,How"
# result=re.findall('[A-Z]?[a-z]+',s)
# print(result)

# s="HELLO,There,How"
# result=re.findall('[A-Z]?[a-z]+',s)
# print(result)
#####################################
# find a phn number
s = """Its purpose is to allow the telephone number 9876543210 of a subscriber identified by name 
  and address 46846 to be found. The rise of the Internet 5654665 and 56545654651535 smart phones in the 21st
  Century greatly reduced the need for a paper phone book"""


# regex='\d+'
# result=re.search(regex,s)
# print(result)
# or

# regex='\d{10}'   # it wont work
# result=re.findall(regex,s)
# print(result)
# or

# regex='\d{10}\s'
# result=re.findall(regex,s)
# print(result)
# or

# regex='\s\d{10}\s'
# result=re.findall(regex,s)
# print(result)
# or

# regex='\s[0-9]{10}\s'
# result=re.findall(regex,s)
# print(result)

#####################################
# FLAGS
# only use for giving specific condition ,its an optional parameter

# s="""Readers can gain knowledge of what it was like to work in New York City in the early 1900s.
# One of the thing that was especially interesting was that there were no safety laws at work.
# Also,there was a big contrast between the rich and the poor.some
# Readers may not like this book because it very depressing,but it is an
# important event in history to Remember"""
#
# print(s)
# regex='^R'    # consider starting of string
# # flag change the property of the regex,not the functions property
# result=re.search(regex,s)
# print(result)
# result=re.search(regex,s,flags=re.MULTILINE)   # search fn search anywhere,^ searches only starting of string
# print(result)

########################
# s="""Readers can gain knowledge of what it was like to work in New York City in the early 1900s.
# One of the thing that was especially interesting was that there were no safety laws at work.
# Also,there was a big contrast between the rich and the poor.some
# Readers may not like this book because it very depressing,but it is an
# important event in history to Remember"""
#
# regex='^R'
# result=re.match(regex,s,flags=re.MULTILINE)
# print(result)

##############################
# s="""Readers can gain knowledge of what it was like to work in New York City in the early 1900s.
# One of the thing that was especially interesting was that there were no safety laws at work.
# Also,there was a big contrast between the rich and the poor.some
# Readers may not like this book because it very depressing,but it is an
# important event in history to Remember"""

# regex='^R'   # normally it consider starting of string
# result=re.findall(regex,s)
# print(result)

# result=re.findall(regex,s,flags=re.MULTILINE)    # here check all new lines starting,otherwise only consider starting of string(since ^)
# print(result)

##############################
# s="""Readers can gain knowledge of what it was like to work in New York City in the early 1900s.
# One of the thing that was especially interesting was that there were no safety laws at work.
# Also,there was a big contrast between the rich and the poor. read some
# Readers may not like this book because it very depressing,but it is an
# important event in history to Remember"""

# regex='Read'
# # result=re.findall(regex,s)
# result=re.findall(regex,s,flags=re.IGNORECASE)   # it consider both lower and uppercase
# print(result)

#############################
# find a ohn number starts with 987

# s="9876543210 46846 5654665 98745654651"
# regex='^987\d{7}'
# regex='\s?[9][8][7]\d{7}\s'
# number=re.findall(regex,s)
# print(number)

##############################
# phn number validation 996
# is the number starting with 996
# s="9967543210"
# regex='^(996)\d{7}$'
# test=re.match(regex,s)
# print(test)
# if test:
#     print("yes,starts with 996")

###############################
# s="9874565455 987654321056 46846 5654665 9874565465 7745654655"
# ph=s.split()
# # print(ph)
# regex='[9][8][7]\d{7}$'
#
# l=[]
# for i in ph:
#     res=re.findall(regex,i)
#     if len(res)!=0:
#         l.append(res)
# print(l)
# for j in l:
#     print(j[0])

###################################
# email validation
# A="abcd123@gmail.com , abcd123@yahoo.in"
# regex='\w+\W\w+\W\w+'
# regex='\w+@\w+[.]{1}\w{2,3}$'
# email=re.findall(regex,A)
# print(email)

##################################
# a=[]
# print("enter 5 inputs")
# for i in range(0,5):
#     a.append(input())
# print(a)
###############################
# create classes PERSON as parent class,and USER as child class.
# parent class instance variables are name,age,mob no
# child class instance variables are username and password.
# input all data from user and create a list
# using this list create an object user1 in which
# user name must be characters and passsword must digits or characters
# create a main fn to check this conditions then if satisfy,create an object user1

# class person:
#     def __init__(self,name,age,mobileno):
#         self.name=name
#         self.age=age
#         self.mobileno=mobileno
# class user(person):
#     def __init__(self,name,age,mobileno,username,password):
#         super().__init__(name,age,mobileno)
#         self.username=username
#         self.password=password
#         print("details:",self.name,self.age,self.password,self.username,self.mobileno)
# def main():
#     a=[]
#     print("Enter name,age,mobile number,user name and password")
#     for i in range(0,5):
#         a.append(input())
#     print(a)
#     # regex = '[a-zA-Z]{5}'
#     # regex = '[a-zA-Z]+'
#     regex = '^[a-zA-Z][a-zA-Z]*[a-zA-Z]$'
#     # regex = '[a-zA-Z0-9]{5,15}'
#     test1 = re.match(regex,a[3])
#     print(a[3])
#     if test1:     # if user name is correct, check for pswd
#         reg='[\da-zA-Z]+[\da-zA-Z]$'
#         test2 = re.match(reg, a[4])
#         if test2:   # if passwd is correct create object
#             user1=user(a[0],a[1],a[2],a[3],a[4])
#         else:
#             print("password must be digits or alphabets")
#     else:
#         print("user name must be  alphabets")
#
# main()

#########################################
# add +91 to the mobile number using lambda fn in the main fn
# class person:
#     def __init__(self,name,age,mobileno):
#         self.name=name
#         self.age=age
#         self.mobileno=mobileno
# class user(person):
#     def __init__(self,name,age,mobileno,username,password):
#         super().__init__(name,age,mobileno)
#         self.username=username
#         self.password=password
#         print("details:",self.name,self.age,self.password,self.username,self.mobileno)
# def main():
#     users=[]
#     a=[]
#     print("Enter name,age,mobile number,user name and password")
#     for i in range(0,5):
#         a.append(input())
#     print(a)
#     regex = '^[a-zA-Z][a-zA-Z]*[a-zA-Z]$'
#     test1 = re.match(regex,a[3])
#     if test1:     # if user name is valid, check for pswd
#         reg='[\da-zA-Z]+'
#         test2 = re.match(reg, a[4])
#         if test2:   # if paswd is correct create object
#             user1=user(a[0],a[1],a[2],a[3],a[4])
#             users.append(user1)
#         else:
#             print("password must be digits or alphabets")
#     else:
#         print("usre name must be alphabets")
#     user2=user("A",12,"1234","abc","a123")
#     user3=user("B",15,"558662","DCG","dm12")
#     users.append(user2)
#     users.append(user3)
#     print(users)   #it get object in list
#     k=map(lambda i:"+91"+i.mobileno,users)  #   add +91 to the mobile numbers using map
#     print(k)
#     for j in k:
#         print(j)
# main()

#########################################
