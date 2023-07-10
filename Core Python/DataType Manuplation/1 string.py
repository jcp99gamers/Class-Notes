#STRING SLICING
a="hello world"
print(a[4])
print(a[:])
print(a[1:])
print(a[1:4])
print(a[1:8:2])
print(a[8:6:1])
print(a[::2])#string slicing
print(a[0:len(a):2])
print(a[-1])
print(a[-3:-1])#backward slice
print(a[-5:-1])
print(a[::-1])#it revise the characters
#####

a="hello world"
a[4]="s"   #we cant change the string,string is imutable
print(a)
del a #we can delete a string,removable
#
# #CONCATINATION
a="hello"
b="world"
a=a+b
print(a)

# #ITERATION
B="world"
for i in b:
    print(i)
#
# #membership opeartors
print("l" in "hello")
print("m" in "hello")
print("m" not in "hello")
print("hl" in "hello")
# ####
#
print("HELLO".lower())
print("HellO".upper())
# ######
# #SPLIT
s="hello world"
print("hello world".split())
l=s.split( )#another way to split
print(l)
#
#
s="hello,world"
print("hello,world".split())
# l=s.split(",")
# print(l)
a="hello/world"
l=a.split("/")
# print(l)
l=a.split("o")
print(l)
# #####
#
# #JOIN
# print(''.join(["hey","morng"]))
print(' '.join(["hey","morng"]))
# s=','.join("hey","morning")
# print(s)
#
a=["hey","morning"]
print(' '.join(a))
# #####
# #REVERSE
a="eranakulam"
print(reversed(a))
# s=list(reversed(a))
# print(s)
# # b=[::-1]
# print(b)
# #####
#
# #SORTING
a=["zbc","agh","khy"]
# a.sort()
# print(a)
# #sorted fn
# a=["zbc","agh","khy"]
# b=sorted(a)
# print(b)
# print(a)
# #####
#
# #.find fn(find out a chara)
# print("how are you".find('ow'))
# print("how are you".find('o'))
# print("how are you".find('are'))
# #####
#
# #replace a word by another(.replace)
# # print("how are you".replace('how','where'))
# ####
#
# #to capitalize first chara
# a="welcome to rogersoft"
# print(a.capitalize())
# ####
#
# #to align a sttring
# a="welcome to rogersoft"
# print(a.center(50,"*"))
# ####
#
# #to count num of chara
# print(a.count("o"))
# print(a.count("om"))
# ####
# #check starting & ending of the string
print(a.startswith("w"))
print(a.startswith("W"))
print(a.endswith("b"))
# #####
#
#to know position of particular chara
print(a.index("c"))
print(a.index("o"))
# #####
#
# #to check whether lower or upper case
# a="welcome to expertzlab"
# print(a.islower())
# print(a.isupper())
# #####
#
# #print words in alphabetical order
str="Hi world how are you"
word=str.lower()
print(word)
words=word.split()
print(words)
words.sort()
print(words)
for w in words:
    print(w)
# #####
#
# #STRIP(remove white space)
# str="Hi world how are you"
# print(str)
# print(len(str))
# s=str.strip()
# print(len(s))
# print(s)
# ##
#
# str="Hi world how are you"
# print(len(str))
# s=str.strip("u")
# print(len(s))
# print(s)
# ##
#
# str="uHi world how are you"
# print(str)
# print(len(str))
# s=str.strip("u")
# print(len(s))
# ##
#
# str="uHi world how are you"
# print(len(str))
# s=str.lstrip("uHi")
# print(len(s))
# print(s)
#
# str="Hi world how are youuuuuuu"
# print(len(str))
# s=str.rstrip("u")
# print(len(s))
# print(s)













