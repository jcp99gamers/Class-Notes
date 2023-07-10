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