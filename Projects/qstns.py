# 1.write a python program that matches a string that has an a followed by three b
# import re
# line="wesbbbavbbba"
# r=re.findall('bbba',line)
# print(r)


# 2.write a python script to concatenate following dictionaries to create a new one
# sample dictionary:
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# # expected result={1:10,2:20,3:30,4:40,5:50,6:60}
#
# expecteddic={}
# expecteddic.update(dic1)
# expecteddic.update(dic2)
# expecteddic.update(dic3)
# print(expecteddic)


# 3. write a python program to filter a list of integers using lambda fn
# original list of integers=[1,2,3,4,5,6,7,8,9,10]
# even numbers=[2,4,6,8,10]
# odd numbers=[1,3,5,7,9]

# l=[1,2,3,4,5,6,7,8,9,10]
# new=list(filter(lambda x:x%2==0,l))
# new1=list(filter(lambda x:x%2!=0,l))
# print(new)
# print(new1)


# 4.write a python program to check if number is prime or not
# num=int(input("enter a number"))
# isDivisible=False
# i=2
# while i<num:
#     if num%i==0:
#         isDivisible=True
#     i+=1
# if isDivisible:
#     print("it's  not a prime number")
# else:
#     print("it's a prime number")
#####
# n = 7
#
# if n > 1:
#     for i in range(2, n):
#         if (n%i)==0:
#             print(n, "is not a prime number")
#             break
#     else:
#         print(n, "is a prime number")
#
# else:
#     print(n, "is not a prime number")



# 5.write a python prgm to construct the following pattern,using nested for loop
# *
# * *
# * * *
# * * * *
# * * * * *

# x=5
# for i in range(1,x+1):
# 	for j in range(1,i+1):
# 		print('*',end=' ')   #Python’s print() function comes with a parameter called ‘end’
#                                 # You can end a print statement with any character/string using this parameter.
# 	print()


# 6.write a python prgm(function)that takes a list and
# returns a new list that contains all the elements of the first
# list minus all the duplicates
# a=[1,2,3,4,35,5,9,2,1]
# def dupe(x):
#     y=[]
#     for i in x:
#         if i not in y:
#             y.append(i)
#     return y
# print(dupe(a))

# # #this one uses sets
# def dupe2(x):
#     return list(set(x))
# print(dupe2(a))
#
#
# print(dict.fromkeys(a))
# mylist = list(dict.fromkeys(a))
# print(mylist)




# 7.create a prgm that asks the user to enter their name and
# their age .print out a message addressed to them that tells them
# the year that they will turn 100 years old

# name=input("what is your name:")
# age=int(input("how old are you"))
# year=str((2021-age)+100)
# print(name+" will be 100 years old in the year"+year)

# or
# from datetime import date
#
# Name=input("Enter the name: ")
# Age=int(input("How old are you: "))
# print("The year when you turn 100 is: ",date.today().year-Age+100)



# 8.	Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player
# plays (using input), compare them, print out a message of congratulations
# to the winner, and ask if the players want to start a new game)
# Remember the rules:
# ●	Rock beats scissors
# ●	Scissors beats paper
# ●	Paper beats rock

# def compare(u1,u2):
#     if u1==u2:
#         return ("it is a tie")
#     elif u1=='rock':
#         if u2=='scissors':
#             return ("rock wins")
#         else:
#             return ("paper wins")
#     elif u1=='scissors':
#         if u2=='paper':
#             return ("scissors win!")
#         else:
#             return ("rock wins!")
#     elif u1=='paper':
#         if u2=='rock':
#             return ("paper wins!")
#         else:
#             return ("scissors wins")
#     else:
#         return ("invalid input! you have not entered rock,paper or scissors,try again.")
#
#
# while True:
#     user1 = input("What's your name?")
#     user2 = input("And your name?")
#     user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
#     user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)
#     print(compare(user1_answer, user2_answer))
#     Ans=input("Do you want to continue? (Y/N)")
#     if Ans=='N':
#         break



# 9.check whether two strings are anagrams of each
# anagrams:a word ,phrase,or name formed by rearranging the letters of another,such as spar,formed from rasp.

# def solve(s,t):
#     if len(s)!=len(t):
#         return False
#
#     s=sorted(s)
#     t=sorted(t)
#
#     return s==t
# s="bite"
# t="biet"
# print(solve(s,t))


# 10.write a program to check whether a string contains all unique characters
# x=input("enter the word")
# l=[]
# for i in x:
#     l.append(i)
# m=[]
# for j in l:
#     if j not in m:
#         m.append(j)
# print(m)
# if len(m)==len(l):
#     print("the string ",x," contains unique characters")
# else:
#     print("the string ",x," contains duplicate characters")

# or

# def check_unique(str):
#     for i in range(len(str)):
#         for j in range(i + 1,len(str)):
#             if(str[i] == str[j]):
#                 return False
#     return True

# str = input("Enter the word: ")
# if(check_unique(str)):
#     print("THE STRING ",str," CONTAINS UNIQUE CHARACTERS")
# else:
#     print("THE STRING ",str," CONTAINS DUPLICATE CHARACTERS")


# 11.write a python program to swap keys and values in a dictionary
# old_dict={'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23}
#
# print("original dictionary is:",old_dict)
# new_dict={}
# for key,value in old_dict.items():
#     if value in new_dict:
#         new_dict[value].append(key)
#     else:
#         new_dict[value]=[key]
#
# print("dictionary after swapping is: ")
# print("keys:values")
# print(new_dict)


# 12.write a python program to change a given string to a new string
# where the first and last chars heve been exchanged
# s=input('enter a string:')
# temp=s[0]
# temp2=s[-1]
# final=temp2+s[1:-1]+temp
# print(final)

# or

# def changestring(str1):
#     return str1[-1]+str1[1:-1]+str1[:1]
#
# print(changestring('abcd'))



# 13.write a python program to find the second most repeated word in a given string
text="""Welcome to ExpertzLab Empowering People,
Committed to Deliver the latest Technoloiges with utmost Quality.
We are a pool of IT professionals and entrepreneurs with more than 20+
years of industry experience. ExpertzLab was found
with the sole intention to cater IT sector with enough IT skills."""
# s=[]
# for words in text.strip(".").split():
#     s.append(words)
#
# dict={}
# for i in s:
#     a=s.count(i)
#     dict.update({i:a})
# print(dict)
# s=[]
# for key,var in dict.items():
#     s.append(var)
# s.sort()
# print(s)
# sec_most_repeated = s[len(s) - 2]
# print(sec_most_repeated)
# for key, var in dict.items():
#     if var == sec_most_repeated:
#         print(key)
#
# # or
#
# def wordCount(str):
#     counts = dict()
#     words = str.split()
#     # print(words)
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#
#     counts_x = sorted(counts.items(),key=lambda k: k[1])
#     print(counts_x)
#
#     return counts_x[-2]
#
# print(wordCount(text))



# 14.twin primes are pairs of primes which differ by two.
# the first twin primes are {3,5},{5,7},{11,13}
# write a python program to generate twin prime numbers less than 100

# def isPrime(n):
#    for i in range(2, n):
#       if n % i == 0:
#          return False
#    return True
#
# def PrimeTwins(start, end):
#    for i in range(start, end):
#       j = i + 2
#       if(isPrime(i) and isPrime(j)):
#          print("{:d} and {:d}".format(i, j))

# PrimeTwins(2, 100)



# 15.write a program to build a simple student management system using python which can perform
# following operations:
# 1.Accept
# 2.Display
# 3.Search
# 4.Delete
# 5.Update
# Accept – This method takes details from the user like name, roll number, and marks for two different subjects.
# Display – This method displays the details of every student.
# Search – This method searches for a particular student from the list of students.
# This method will ask the user for roll number and then search according to the roll number
# Delete – This method deletes the record of a particular student with a matching roll number.
# Update – This method updates the roll number of the student.
# This method will ask for the old roll number and new roll number. It will replace the old roll number
# with new roll number.

# class Student:
#     def __init__(self,name,rollno,m1,m2):
#         self.name=name
#         self.rollno=rollno
#         self.m1=m1
#         self.m2=m2
#     def accept(self):
#         ls.append(self)
#     def display(self):
#         print("Name:",self.name)
#         print("RollNo:",self.rollno)
#         print("mark1:",self.m1)
#         print("mark2:",self.m2)
#         print("\n")
#     def search(self,rn):
#         for i in range(ls.__len__()):
#             if (ls[i].rollno==rn):
#                 return i
#
#     def delete(self,rn):
#         i=self.search(rn)
#         del ls[i]
#     def update(self,rn,No):
#         i=self.search(rn)
#         roll=No
#         ls[i].rollno=roll
#
# ls=[]
# obj1=Student("A",1,100,100)
# obj2=Student("B",2,90,90)
# obj3=Student("C",3,80,80)
# print("\nOperations used :")
# print("\n1.Accept student details\n2.Display Student Details\n"
#       "3.Search Details of a student\n4.Delete details of student"
#       "\n5.Update student Details")
# ch=int(input("Enter choice :"))
# if (ch==1):
#     obj1.accept()
#     obj2.accept()
#     obj3.accept()
#     print(ls)
#
# elif(ch==2):
#     print("\n")
#     print("\nStudent Details:")
#     obj1.accept()
#     obj2.accept()
#     obj3.accept()
#     for i in ls:
#         i.display()
# elif(ch==3):
#     obj1.accept()
#     obj2.accept()
#     obj3.accept()
#     print("\nStudent Found :")
#     a=int(input("enter a roll no :"))
#     print(obj1.search(a))
#
# elif(ch==4):
#     obj1.accept()
#     obj2.accept()
#     obj3.accept()
#     a = int(input("enter a roll no to delete :"))
#     obj1.delete(a)
#     print("List of students after deletion")
#     for i in ls:
#         i.display()
#
# elif(ch==5):
#     obj1.accept()
#     obj2.accept()
#     obj3.accept()
#     a=int(input("enter old roll no:"))
#     b=int(input("enter new roll no:"))
#     obj1.update(a,b)
#     print("List of students after updation")
#     for i in ls:
#         i.display()
#
# else:
#     print(" Thank you !")



