#list is mutable&indexable####
# # ##creating a list##
# ist method
# L=[1,2,3,4,5,6,7,8,9]
# print(type(L))
# 2nd method
# A=[]#empty list
# print(A)
# print(type(A))#to check type
# S="jhcdgu swuhdi"
# l=list(S)
# print(l)
# print(len(l))#length checking
# ###################################
# ##list slicing##
# L=[1,2,3,4,2,5,2,6,7,8,9]
# print(L[0])
# print(L[4])
# print(L[:])  # same as print(l)
# print(L[:5])
# print(L[2:5])
# print(L[2:10:2])
# print(L[::2])
# print(L[0:15:2])
# print(L[0:len(L):2])#full length
# print(L[0::2])
# print(L[-1])
# print(L[-2])
# L=[1,2,3,4,2,5,2,[6,7,8,9]]
# print(L[7])
# print(L[7][0])
# print(L[-1][0])
# print(L[-1][-1])
# ###################################
# ##list concatinationn###

# new=L+K
# new=K+L
# print(new)
# #################################
# ###Assign value to index#########
# L=[1,2,3,4,2,5,2,6,7,8,9]
# L[6]="five"
# print(L)
# #########################
# ##Adding as last element###
# print(len(L))
# L.append("FIVE")
# print(l)
#
# ###########################
# ##INSERTING IN TO A PERTICULAR POSITION##
# L=[1,2,3,4,2,5,2,6,7,8,9]
# L.insert(3,"three")##To add three in 3rd postion
# print(L)
# print(L.index("three"))### to check position
# print(L.index(2))
# ################################
# ##remove methods##
# del L
# print(L)
# ###############
# #remove
# L=[1,2,3,4,2,5,2,6,7,8,9]
# L.remove(2) #remove first occrnce of element
# print(L)
# del L[3] ## 3rd postion elm
# print(L)
# ##############
# #pop
# L=[1,2,3,4,2,5,2,6,7,8,9]
# print(L)
# L.pop(4)#in pop method the value is return and del/we can assign that value in a variable
# a=L.pop(3)
# print(a)
# print(L)
# ##############################
# ##adding elements to the list
# L=[1,2,3,4,2,5,2,6,7,8,9]
# b=["a","b","c"]# list
# c=("a","b","c")# we can also extend tuple
# L.extend(c)
# print(c)
# L.append(c)
# print(L)
# L.extend(b)#it add as elements in L
# print(L)
# L.append(b)## the elements add as a list
# print(L)
# ################################
# ##count##
# L=[1,2,3,4,2,5,2,6,7,8,9]
# print(L.count(6))
# print(L.count(2))
# ######################
# ##to make empty list##
# L.clear()##to remove elements
# print(L)
# ###################
# ##to copy a list to another variable##
# L=[1,2,3,4,2,5,2,6,7,8,9]
# s=L.copy()
# print(s)
# K=L#same as copy
# print(K)
# s=L[2:5].copy() #copy a portion
# print(s)
# print(K)
# ############################
# ##membership operator##
L=[1,2,3,4,2,"three",5,2,6,7,8,9]
if "three" in L:
    print("it is there in the list")
if 10 not in L:
    print("empty")
# #######################
# s=[1,5,4,9,6,8,0]
# s.sort()
# print(s)
# #####################
# v=sorted(s,reverse=True)#descending order
# print(v)
# print(s)
# #########################
# ##iteration##
# for i in s:
#     print(i)
# #######################
# t="hello world HELLOW WORLD"
# a=t.split( )
# print(a)

# t="hello,world,HELLOW,WORLD"
# a=t.split(",")
# print(a)
# ###############
# find square of the list
# t=[0,1,2,3,4,5,6,7,8,9,10]
# s=[]
# for i in t:
#     s.append(i**2)
# print(s)
# ###or##
# for i in range(11):
#     print(i)
#     s.append(i**2)
# print(s)
#####

# create list of  all positive num
# lst=[-10,-20,10,20,-15,30]
# s=[]
# for i in lst:
#     if i>=0:
#         s.append(i)
# print(s)
#####


# write a program to find largest number from the list
l=[45,8,6,89,7,15,35,100]
# l.sort()
# # print(l)
# print(l[-1])
##or

# large=l[0]
# for i in l:
#     if i>large:
#         large=i
# print(large)
#####






# 1.write a program to count number of strings which have first and last element are same
l=["xyz","aba","abcd","1231","sdhbks"]
# count=0
# for i in l:
#     if i[0]==i[-1]:
#         count=count+1
# print(count)
######

# 2.write a program to remove duplicate items from the list
l=[10,20,30,20,10,50,10]
for i in l:
    if l.count(i)>1:
        l.remove(i)
print(l)
##or
# b=[]
# for i in l:
#     if i not in b:
#         b.append(i)
#     # print(b)
# print(b)
######
#reverse
l=[1,45,8,9,9]
l.reverse()
print(l)
# ####
# #aggrigate fn
# l=[0,1,2,3,4,5,6,7,8,9,10]
# print(max(l))
# print(sum(l))
# print(min(l))
#######

#nested list
l=[[0,1,2],[3,4,5,6],[7,8,9,10]]
print(l[1])
print(l[2][1])
print(l[1][1])
######

#list comprehesion
# sqrs=[]
# for i in range(5):
#     sqrs.append(i**2)
# print(sqrs)
######

#print positive num from the list in comprehension method
l=[-10,-20,9,45,-33]
s=[i for i in l if i>=0]
print(s)
###########
#transpose of matrix
m=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12]]
# l=[[0,0,0,],
#    [0,0,0],
#    [0,0,0],
#    [0,0,0]]
# for i in range(len(m)):
#     for j in range(len(m[0])):
#          l[j][i] = m[i][j]
# for k in l:
#     print(k)
###or
t=[]
for i in range(4):
    lst=[]
    for row in m:
        lst.append(row[i])
    t.append(lst)
print(t)
#########

