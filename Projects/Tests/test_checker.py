import importlib.util

# define test cases with input and expected output
test_cases1 = [
  {
    'input': [['chi',20.0],['beta',50.0],['alpha',50.0]],
    'expected_output': ['alpha', 'beta']
  },
  {
    'input': [['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]],
    'expected_output': ['Berry', 'Harry']
  },
  {
  'input': [],
  'expected_output': []
  },
  {
  'input': [['John', 40]],
  'expected_output': []
  },
  {
  'input': [['John', 40], ['Jane', 40], ['Bob', 40]],
  'expected_output': []
  },
  {
  'input': [['John', 30], ['Jane', 40], ['Bob', 50]],
  'expected_output': ['Jane']
  },
  {
  'input': [['John', 50], ['Jane', 30], ['Bob', 40], ['Jack', 50], ['Jill', 20]],
  'expected_output': ['Jane']
  },
  {
  'input': [['John', 30], ['Jane', 40], ['Bob', 40], ['Jack', 50], ['Jill', 30], ['Jim', 50]],
  'expected_output': ['Bob', 'Jane']
  },
  {
  'input': [['Zack', 40], ['Yolanda', 40], ['Xander', 40], ['Wendy', 40], ['Vikram', 40], ['Ursula', 40]],
  'expected_output': []
  },
  {
  'input': [['John', 30], ['Ursula', 40], ['Vikram', 40], ['Wendy', 40], ['Xander', 40], ['Yolanda', 40], ['Zack', 40]],
  'expected_output': ['Ursula', 'Vikram', 'Wendy', 'Xander', 'Yolanda', 'Zack']
  },
  {
  'input': [['Adam', 90], ['Bob', 80], ['Charlie', 70], ['David', 80], ['Emily', 60]],
  'expected_output': ['Charlie']
  },
  {
  'input': [['Alice', 80], ['Bob', 90], ['Charlie', 80], ['David', 70], ['Emily', 60], ['Fred', 90]],
  'expected_output': ['David']
  },
  {
  'input': [['Victor', 70], ['Wendy', 70], ['Xander', 70], ['Yara', 70], ['Zoe', 70]],
  'expected_output': []
  },
  {
  'input': [['Adam', 80], ['Bob', 70], ['Charlie', 70], ['David', 60], ['Emily', 60], ['Frank', 50]],
  'expected_output': ['David', 'Emily']
  },
  {
  'input': [['Alice', 100], ['Bob', 90], ['Charlie', 80], ['David', 70], ['Emily', 60], ['Fred', 50]],
  'expected_output': ['Emily']
  }
]
test_cases2 = [
  {
    'input': ([30, 6, 4, 1],96),
    'expected_output': [30,30,30,6]
  },
  {
    'input': ([30, 6, 4, 1],97),
    'expected_output': [30,30,30,6,1]
  },
  {
    'input': ([30, 6, 4, 1],98),
    'expected_output': [30,30,30,4,4]
  },
  {
    'input': ([30, 6, 4, 1],99),
    'expected_output': [30,30,30,4,4,1]
  },
  {
    'input': ([30, 6, 4, 1],100),
    'expected_output': [30,30,30,6,4]
  },
]
test_cases3 = [{'input': 1, 'expected_output': False}, {'input': 2, 'expected_output': True}, {'input': 3, 'expected_output': False}, {'input': 4, 'expected_output': True}, {'input': 5, 'expected_output': False}, {'input': 6, 'expected_output': True}, {'input': 7, 'expected_output': False}, {'input': 8, 'expected_output': True}, {'input': 9, 'expected_output': False}, {'input': 10, 'expected_output': True}, {'input': 11, 'expected_output': True}, {'input': 12, 'expected_output': True}, {'input': 13, 'expected_output': False}, {'input': 14, 'expected_output': True}, {'input': 15, 'expected_output': False}, {'input': 16, 'expected_output': True}, {'input': 17, 'expected_output': False}, {'input': 18, 'expected_output': True}, {'input': 19, 'expected_output': False}, {'input': 20, 'expected_output': False}, {'input': 21, 'expected_output': False}, {'input': 22, 'expected_output': True}, {'input': 23, 'expected_output': False}, {'input': 24, 'expected_output': False}, {'input': 25, 'expected_output': False}, {'input': 26, 'expected_output': False}, {'input': 27, 'expected_output': False}, {'input': 28, 'expected_output': False}, {'input': 29, 'expected_output': False}, {'input': 30, 'expected_output': False}, {'input': 31, 'expected_output': False}, {'input': 32, 'expected_output': False}, {'input': 33, 'expected_output': True}, {'input': 34, 'expected_output': False}, {'input': 35, 'expected_output': False}, {'input': 36, 'expected_output': False}, {'input': 37, 'expected_output': False}, {'input': 38, 'expected_output': False}, {'input': 39, 'expected_output': False}, {'input': 40, 'expected_output': False}, {'input': 41, 'expected_output': False}, {'input': 42, 'expected_output': False}, {'input': 43, 'expected_output': False}, {'input': 44, 'expected_output': True}, {'input': 45, 'expected_output': False}, {'input': 46, 'expected_output': False}, {'input': 47, 'expected_output': False}, {'input': 48, 'expected_output': False}, {'input': 49, 'expected_output': False}, {'input': 50, 'expected_output': False}, {'input': 51, 'expected_output': False}, {'input': 52, 'expected_output': False}, {'input': 53, 'expected_output': False}, {'input': 54, 'expected_output': False}, {'input': 55, 'expected_output': True}, {'input': 56, 'expected_output': False}, {'input': 57, 'expected_output': False}, {'input': 58, 'expected_output': False}, {'input': 59, 'expected_output': False}, {'input': 60, 'expected_output': False}, {'input': 61, 'expected_output': False}, {'input': 62, 'expected_output': False}, {'input': 63, 'expected_output': False}, {'input': 64, 'expected_output': False}, {'input': 65, 'expected_output': False}, {'input': 66, 'expected_output': True}, {'input': 67, 'expected_output': False}, {'input': 68, 'expected_output': False}, {'input': 69, 'expected_output': False}, {'input': 70, 'expected_output': False}, {'input': 71, 'expected_output': False}, {'input': 72, 'expected_output': False}, {'input': 73, 'expected_output': False}, {'input': 74, 'expected_output': False}, {'input': 75, 'expected_output': False}, {'input': 76, 'expected_output': False}, {'input': 77, 'expected_output': True}, {'input': 78, 'expected_output': False}, {'input': 79, 'expected_output': False}, {'input': 80, 'expected_output': False}] # [{'input': 1, 'expected_output': False}, {'input': 2, 'expected_output': True}, {'input': 3, 'expected_output': False}, {'input': 4, 'expected_output': True}, {'input': 5, 'expected_output': False}, {'input': 6, 'expected_output': True}, {'input': 7, 'expected_output': False}, {'input': 8, 'expected_output': True}, {'input': 9, 'expected_output': False}, {'input': 10, 'expected_output': True}, {'input': 11, 'expected_output': True}, {'input': 12, 'expected_output': True}, {'input': 13, 'expected_output': False}, {'input': 14, 'expected_output': True}, {'input': 15, 'expected_output': False}, {'input': 16, 'expected_output': True}, {'input': 17, 'expected_output': False}, {'input': 18, 'expected_output': True}, {'input': 19, 'expected_output': False}, {'input': 20, 'expected_output': False}, {'input': 21, 'expected_output': False}, {'input': 22, 'expected_output': True}, {'input': 23, 'expected_output': False}, {'input': 24, 'expected_output': False}, {'input': 25, 'expected_output': False}, {'input': 26, 'expected_output': False}, {'input': 27, 'expected_output': False}, {'input': 28, 'expected_output': False}, {'input': 29, 'expected_output': False}, {'input': 30, 'expected_output': False}, {'input': 31, 'expected_output': False}, {'input': 32, 'expected_output': False}, {'input': 33, 'expected_output': True}, {'input': 34, 'expected_output': False}, {'input': 35, 'expected_output': False}, {'input': 36, 'expected_output': False}, {'input': 37, 'expected_output': False}, {'input': 38, 'expected_output': False}, {'input': 39, 'expected_output': False}, {'input': 40, 'expected_output': False}, {'input': 41, 'expected_output': False}, {'input': 42, 'expected_output': False}, {'input': 43, 'expected_output': False}, {'input': 44, 'expected_output': True}, {'input': 45, 'expected_output': False}, {'input': 46, 'expected_output': False}, {'input': 47, 'expected_output': False}, {'input': 48, 'expected_output': False}, {'input': 49, 'expected_output': False}, {'input': 50, 'expected_output': False}, {'input': 51, 'expected_output': False}, {'input': 52, 'expected_output': False}, {'input': 53, 'expected_output': False}, {'input': 54, 'expected_output': False}, {'input': 55, 'expected_output': True}, {'input': 56, 'expected_output': False}, {'input': 57, 'expected_output': False}, {'input': 58, 'expected_output': False}, {'input': 59, 'expected_output': False}, {'input': 60, 'expected_output': False}, {'input': 61, 'expected_output': False}, {'input': 62, 'expected_output': False}, {'input': 63, 'expected_output': False}, {'input': 64, 'expected_output': False}, {'input': 65, 'expected_output': False}, {'input': 66, 'expected_output': True}, {'input': 67, 'expected_output': False}, {'input': 68, 'expected_output': False}, {'input': 69, 'expected_output': False}, {'input': 70, 'expected_output': False}, {'input': 71, 'expected_output': False}, {'input': 72, 'expected_output': False}, {'input': 73, 'expected_output': False}, {'input': 74, 'expected_output': False}, {'input': 75, 'expected_output': False}, {'input': 76, 'expected_output': False}, {'input': 77, 'expected_output': True}, {'input': 78, 'expected_output': False}, {'input': 79, 'expected_output': False}, {'input': 80, 'expected_output': False}, {'input': 81, 'expected_output': False}, {'input': 82, 'expected_output': False}, {'input': 83, 'expected_output': False}, {'input': 84, 'expected_output': False}, {'input': 85, 'expected_output': False}, {'input': 86, 'expected_output': False}, {'input': 87, 'expected_output': False}, {'input': 88, 'expected_output': True}, {'input': 89, 'expected_output': False}, {'input': 90, 'expected_output': False}, {'input': 91, 'expected_output': False}, {'input': 92, 'expected_output': False}, {'input': 93, 'expected_output': False}, {'input': 94, 'expected_output': False}, {'input': 95, 'expected_output': False}, {'input': 96, 'expected_output': False}, {'input': 97, 'expected_output': False}, {'input': 98, 'expected_output': False}, {'input': 99, 'expected_output': True}, {'input': 100, 'expected_output': False}, {'input': 101, 'expected_output': True}, {'input': 102, 'expected_output': False}, {'input': 103, 'expected_output': False}, {'input': 104, 'expected_output': False}, {'input': 105, 'expected_output': False}, {'input': 106, 'expected_output': False}, {'input': 107, 'expected_output': False}, {'input': 108, 'expected_output': False}, {'input': 109, 'expected_output': False}, {'input': 110, 'expected_output': True}, {'input': 111, 'expected_output': False}, {'input': 112, 'expected_output': False}, {'input': 113, 'expected_output': False}, {'input': 114, 'expected_output': False}, {'input': 115, 'expected_output': False}, {'input': 116, 'expected_output': False}, {'input': 117, 'expected_output': False}, {'input': 118, 'expected_output': False}, {'input': 119, 'expected_output': False}, {'input': 120, 'expected_output': False}, {'input': 121, 'expected_output': True}, {'input': 122, 'expected_output': False}, {'input': 123, 'expected_output': False}, {'input': 124, 'expected_output': False}, {'input': 125, 'expected_output': False}, {'input': 126, 'expected_output': False}, {'input': 127, 'expected_output': False}, {'input': 128, 'expected_output': False}, {'input': 129, 'expected_output': False}, {'input': 130, 'expected_output': False}, {'input': 131, 'expected_output': False}, {'input': 132, 'expected_output': True}, {'input': 133, 'expected_output': False}, {'input': 134, 'expected_output': False}, {'input': 135, 'expected_output': False}, {'input': 136, 'expected_output': False}, {'input': 137, 'expected_output': False}, {'input': 138, 'expected_output': False}, {'input': 139, 'expected_output': False}, {'input': 140, 'expected_output': False}, {'input': 141, 'expected_output': True}, {'input': 142, 'expected_output': False}, {'input': 143, 'expected_output': True}, {'input': 144, 'expected_output': False}, {'input': 145, 'expected_output': False}, {'input': 146, 'expected_output': False}, {'input': 147, 'expected_output': False}, {'input': 148, 'expected_output': False}, {'input': 149, 'expected_output': False}, {'input': 150, 'expected_output': False}, {'input': 151, 'expected_output': False}, {'input': 152, 'expected_output': False}, {'input': 153, 'expected_output': False}, {'input': 154, 'expected_output': True}, {'input': 155, 'expected_output': False}, {'input': 156, 'expected_output': False}, {'input': 157, 'expected_output': False}, {'input': 158, 'expected_output': False}, {'input': 159, 'expected_output': False}, {'input': 160, 'expected_output': False}, {'input': 161, 'expected_output': True}, {'input': 162, 'expected_output': False}, {'input': 163, 'expected_output': False}, {'input': 164, 'expected_output': False}, {'input': 165, 'expected_output': True}, {'input': 166, 'expected_output': False}, {'input': 167, 'expected_output': False}, {'input': 168, 'expected_output': False}, {'input': 169, 'expected_output': False}, {'input': 170, 'expected_output': False}, {'input': 171, 'expected_output': False}, {'input': 172, 'expected_output': False}, {'input': 173, 'expected_output': False}, {'input': 174, 'expected_output': False}, {'input': 175, 'expected_output': False}, {'input': 176, 'expected_output': True}, {'input': 177, 'expected_output': False}, {'input': 178, 'expected_output': False}, {'input': 179, 'expected_output': False}, {'input': 180, 'expected_output': False}, {'input': 181, 'expected_output': True}, {'input': 182, 'expected_output': False}, {'input': 183, 'expected_output': False}, {'input': 184, 'expected_output': False}, {'input': 185, 'expected_output': False}, {'input': 186, 'expected_output': False}, {'input': 187, 'expected_output': True}, {'input': 188, 'expected_output': False}, {'input': 189, 'expected_output': False}, {'input': 190, 'expected_output': False}, {'input': 191, 'expected_output': False}, {'input': 192, 'expected_output': False}, {'input': 193, 'expected_output': False}, {'input': 194, 'expected_output': False}, {'input': 195, 'expected_output': False}, {'input': 196, 'expected_output': False}, {'input': 197, 'expected_output': False}, {'input': 198, 'expected_output': True}, {'input': 199, 'expected_output': False}, {'input': 200, 'expected_output': False}, {'input': 201, 'expected_output': True}, {'input': 202, 'expected_output': True}, {'input': 203, 'expected_output': False}, {'input': 204, 'expected_output': False}, {'input': 205, 'expected_output': False}, {'input': 206, 'expected_output': False}, {'input': 207, 'expected_output': False}, {'input': 208, 'expected_output': False}, {'input': 209, 'expected_output': False}, {'input': 210, 'expected_output': False}, {'input': 211, 'expected_output': False}, {'input': 212, 'expected_output': False}, {'input': 213, 'expected_output': False}, {'input': 214, 'expected_output': False}, {'input': 215, 'expected_output': False}, {'input': 216, 'expected_output': False}, {'input': 217, 'expected_output': False}, {'input': 218, 'expected_output': False}, {'input': 219, 'expected_output': False}, {'input': 220, 'expected_output': False}, {'input': 221, 'expected_output': True}, {'input': 222, 'expected_output': True}, {'input': 223, 'expected_output': False}, {'input': 224, 'expected_output': False}, {'input': 225, 'expected_output': False}, {'input': 226, 'expected_output': False}, {'input': 227, 'expected_output': False}, {'input': 228, 'expected_output': False}, {'input': 229, 'expected_output': False}, {'input': 230, 'expected_output': False}]

test_caseDict = {
    "test1":test_cases1,
    "test2":test_cases2,
    "test3":test_cases3,
}

passed = 0
failed = []
j = 0
for fileNum, testCase in test_caseDict.items():
  # specify the file and function to test
  file_to_test = f'{fileNum}.py'
  function_to_test = 'main'
  # load the module containing the function to test
  spec = importlib.util.spec_from_file_location('module.name', file_to_test)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  # loop through the test cases and run the function on each input
  for i, test_case in enumerate(testCase):
    input_data = test_case['input']
    expected_output = test_case['expected_output']
    # call the function and check the result
    if tuple == type(input_data):
      result = module.main(*input_data)
    else:  
      result = module.main(input_data)
    j += 1
    if result == expected_output:
      passed += 1
      print(f'Test case {j} passed.')
      # print(f'Test case {i+1} passed.')
    else:
      failed.append({f'{fileNum}.py':i})
      print(f'Test case {j} failed. Expected {expected_output}, but got {result}.')
      # print(f'Test case {i+1} failed. Expected {expected_output}, but got {result}.')

if failed != []:
  print(r'Below are the List Index of the Failed Cases')
  print(failed)
print(f"{passed} OUT OF {j} PASSED")
