"""
Difficulty Medium
File Name = test1.py
Function Name = main
Parameters of Function = records(list)
Sample Input: records = [['chi',20.0],['beta',50.0],['alpha',50.0]]
TO DO:
- Convert the list 'records' to a dictionary 'sample'
- In this Case the dictionary would become "sample = {20.0: ['chi'], 50.0: ['beta', 'alpha']}"
- Get the Second Lowest Value from the Dictionary Keys
- In this Case the value would be "second_lowest = 50.0"
- Then Take the Value Assigned to that Key(second_lowest) and Rearrange them in Ascending Order
- In this Case the value would be "result = ['alpha', 'beta']"
- return that List
"""

def main(records:list):
    '''
    sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
    highest_score = sorted_students[0][1]
    top_students = [student[0] for student in sorted_students if student[1] == highest_score]
    return top_students
    '''
    # records = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     records.append([name,score])
    sample = {}
    for key, value in records:
        if value in sample:
            sample[value].append(key)
        else:
            sample[value] = [key]
    """
    second_lowest = sorted(list(set(grade for name, grade in records)))[1]
    result = sorted(sample[second_lowest])
    print(second_lowest)
    """
    try:
        result = sorted(sample[sorted(list(set(grade for name, grade in records)))[1]])
    except:
        result = []
    # print(sample)
    """
    for name in result:
        print(name)
    """
    # print(result)
    return result