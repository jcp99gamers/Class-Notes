"""
Difficulty Low
File Name = test3.py
Function Name = main
Parameters of Function = number(int)
Sample Input: number = 121
TO DO:
- Need to Figure out if the Number is a special integer
- Special Integer is when adding 2 Numbers together and the 2 Numbers are the Palindrome of Each Other
- eg: 
- 121 = 29+92 (29 is a Number & 92 is the Palindrome of the Number hence 121 is a Special Number)
- 22 is 11+11 (11 is a Number & 11 is the Palindrome of the Number hence 22 is a Special Number)
- There are Many Ways to Solve this Try to make it Optimised.
- return that Boolean (True IF special integer)
"""

def main(number:int):
    # halfNum = int(number/2)
    # halfNum += 1 if number%2 != 0 else 0
    # print(f"N={number}",f"H={halfNum}")
    for a in range(number + 1):
        for b in range(number + 1):
            if b == int(str(a)[::-1]):
                if a + b == number:
                    # print(number,"=",a,"+",b,",",True)
                    return True
    return False

# # Test cases
# test_cases3 = []
# for x in range(1,81):
#     print(x)
#     test_cases3.append({'input':x,'expected_output':main(x)})
# print(test_cases3)