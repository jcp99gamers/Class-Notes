"""
Difficulty Hard
File Name = test2.py
Function Name = main
Parameters of Function = notes(list), totalAmount(int)
Sample Input: notes = [30, 6, 4, 1], totalAmount = 99
TO DO:
- Utilising the Given List we Know what are the Denominations of Notes we have
- We Need to Figure out How to Get the Minimum Number of Notes taken to give the sum totalAmount
- Make the List of the Notes
- return that List
- eg: Test Cases keeping the notes denominations same ([30,6,4,1]) & giving Different Total Amounts the below are the expected results
- 98 => [30,30,30,4,4], 99 => [30,30,30,4,4,1], 100 => [30,30,30,6,4]
- return the List (of Least Number of Notes to get that Sum)
"""

def main(notes:list, totalAmount:int):
    # Initialize the result list
    ListOfLists = []
    AmmountToGet = totalAmount 
    listOfNotes = notes    
    # Define a recursive function to find sublists
    def find_sublist(target, current_list, start_index):
        # Base case: if the target is 0, append the current list to the ListOfLists
        if target == 0:
            ListOfLists.append(current_list)
            return
        # Iterate through the numbers starting from start_index
        for i in range(start_index, len(listOfNotes)):
            # If the current number is less than or equal to the target
            if listOfNotes[i] <= target:
                # Recursively call the function with updated parameters
                find_sublist(target - listOfNotes[i], current_list + [listOfNotes[i]], i)
    # Call the recursive function
    find_sublist(AmmountToGet, [], 0)
    subList =  sorted(ListOfLists, key=lambda x: len(x))
    result = sorted(sorted(subList[0]), reverse=True)
    return result

# # Test cases
# test_cases2 = []
# print([30, 6, 4, 1])
# for x in range(85,100):
#     print(x,"=>",main([30, 6, 4, 1], x))
