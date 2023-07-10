import importlib.util

# define test cases with input and expected output
test_cases = [
  {
    'input': [['chi',20.0],['beta',50.0],['alpha',50.0]],
    'expected_output': ['alpha', 'beta']
  },
  {
    'input': [['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]],
    'expected_output': ['Berry', 'Harry']
  },
  # {
  # 'input': [],
  # 'expected_output': []
  # },
  # {
  # 'input': [['John', 40]],
  # 'expected_output': []
  # },
  # {
  # 'input': [['John', 40], ['Jane', 40], ['Bob', 40]],
  # 'expected_output': []
  # },
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
  # {
  # 'input': [['Zack', 40], ['Yolanda', 40], ['Xander', 40], ['Wendy', 40], ['Vikram', 40], ['Ursula', 40]],
  # 'expected_output': []
  # },
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
  # {
  # 'input': [['Victor', 70], ['Wendy', 70], ['Xander', 70], ['Yara', 70], ['Zoe', 70]],
  # 'expected_output': []
  # },
  {
  'input': [['Adam', 80], ['Bob', 70], ['Charlie', 70], ['David', 60], ['Emily', 60], ['Frank', 50]],
  'expected_output': ['David', 'Emily']
  },
  {
  'input': [['Alice', 100], ['Bob', 90], ['Charlie', 80], ['David', 70], ['Emily', 60], ['Fred', 50]],
  'expected_output': ['Emily']
  }
]

# specify the file and function to test
file_to_test = 'test.py'
function_to_test = 'main'

# load the module containing the function to test
spec = importlib.util.spec_from_file_location('module.name', file_to_test)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# loop through the test cases and run the function on each input
for i, test_case in enumerate(test_cases):
  input_data = test_case['input']
  expected_output = test_case['expected_output']
  
  # call the function and check the result
  result = module.main(input_data)
  
  if result == expected_output:
    print(f'Test case {i+1} passed.')
  else:
    print(f'Test case {i+1} failed. Expected {expected_output}, but got {result}.')

"""
Create a File Named 'test.py'
Create a Function Called 'main'
The Function Should Have a Parameter called 'records' which is Gonna Pass a List
EXAMPLE Input "records = [['chi',20.0],['beta',50.0],['alpha',50.0]]"
Convert the list 'records' to a dictionary 'sample'
In this Case the dictionary would become "sample = {20.0: ['chi'], 50.0: ['beta', 'alpha']}"
Get the Second Lowest Value from the Dictionary Keys
In this Case the value would be "second_lowest = 50.0"
Then Take the Value Assigned to that Key(second_lowest) and Rearrange them in Ascending Order
In this Case the value would be "result = ['alpha', 'beta']"
return that List
"""