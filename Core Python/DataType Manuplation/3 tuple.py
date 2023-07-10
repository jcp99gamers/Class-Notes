 #indexable
#immutable (can't add or delete item)cant modify
t=()
print(type(t))
t=tuple()
print(type(t))
print(t)
t=(1,2,3)
print(type(t))
t=1,2,3
print(type(t))
#########
t=(1)
print(type(t))
t=("a",)
print(type(t))
print(t[0:2])
##############
t=(1,2,3,"a",5.25)
print(type(t))
print(t)
t=(2,3,(4,5))#tuple inside tuple
print(t[2])
print(t[2][0])
##########
t=(2,3,[4,5])#list inside is mutable
print(t[2][0])
t[1]=10#immutable
print(t)
t[2][0]=9
print(t)
t[2]=[4,8,12]
#####
#concatination
clr=('blue','red','orange','yellow')
other=('black','white')
print(id(clr))
clr=clr+other#concatination and form new tuple
print(id(clr))
print(clr)
######
#but in list
l=[1,2,5,2]
print(id(l))
print(l)
b=[3]
l.append(b)
print(id(l)) #both id s are same
print(l)
######
##repeating
t=(('apple',1,2)*4)
print(t)
t=(('apple')*4)
print(t)
#########
del t
print(t)
#####
#count a data
t=(1,2,3,5,8,1,9,4,5,6,2,4,1)
print(t.count(1))
###
#index of instance
print(t.index(5)) #position of 5 in the list
#####
#membership operator
print(9 in t)
#########
#find length
print(len(t))
########
#aggrigate fn
t=(1,2,3,5,8,1,)
print(max(t))
print(sum(t))
print(min(t))
####
#sorting
# t.sort()#not applicable
print(t)
new=sorted(t)
print(new)
for i in t:
    print(i)





