# cannot index(unordered collection of data)athaayath
# storeeynna datakk oru particular order parayan
# pattilla.aa values in bw chelapo randamath
# printeyyokke aanenki kedakkunna position change
# aavum.chelpo same kittum allenki kittananne illa.
# mutable
# empty set
# u={} # it forms a dictionary
# print(type(u))
# u=set()
# print(type(u))
# ##
# a={1,2}
# print(type(a))
# ##
# a=set([1,2,3]) # type conversion
# print(type(a))
# print(a)
##
#to add an element (we can add only single element)
a={1,3,2,7,4,5,6,2,3}
# print(a)   #multiple occurance is not allowed
# a.add("str")  # we cant say the exact position of the value
# print(a)
a.add(0)
print(a)
#########
#update method(add more than one elements)
# a={1,3,2,7,4,5,6,2,3}
a.update("a","b")
# print(a)
# a.update({"a","v",1})
# print(a)
a.update(["b","y"])
# print(a)
#
# a.update(["ann","mary"],{"xyz","ghj"})
# print(a)
######
#remove fn
# # a={1,3,2,7,4,5,6,2,3}
# a.discard(4)
# print(a)
# a.discard("xyz")
# print(a)
# a.remove(5)#removing 5
# print(a)
# a.discard(10)#it will not show an error while the element not in the set
# print(a)
# a.remove(10)#it shows an error
# print(a)
###########
#pop method
a={1,5,8,3}
print(a)
a.pop() #to randomly remove an element
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# x=a.pop()#we can return the value that removed
# print(x)
######
#clear (to clear all elements in the set)
# a={1,3,2,7,4,5,6,2,3}
# a.clear()
# print(a)
########
#aggrigate fn
# a={1,5,8,3}
# print(min(a))
# print(sum(a))
# print(max(a))
########
#sorted fn
# a={1,9,5,8}
# print(sorted(a))
#####
##set operators
#union
set1={1,2,3}
set2={3,4,5}
# print(set1 | set2)
# or
# print(set1.union(set2))
###
#intersection
# print(set1 & set2)
# print(set1.intersection(set2))
####
#difference
# print(set1 - set2)
# print(set1.difference(set2))
###
#symmetric difference
# print(set1 ^ set2)   # (b-a)U(a-b)
#########
#frozen set
# x=frozenset([1,2,3,4,5])
# print(type(x))
# print(x)
# x.add("str") #it is immutable(cant change)
# print(x)
###########



