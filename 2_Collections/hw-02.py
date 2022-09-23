"""
1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""

import random  # Import random module for numbers generation
import string  # Import string module for letters generator

random.seed(a=4)  # Use the same set of random numbers between executions (for debug purpose)

result_list = []  # Initialize empty list for random dicts

for i in range(random.randint(2, 10)):  # Initialize iteration in random range from 2 to 10
    letters_list = string.ascii_lowercase  # Generate list of letters
    count_of_values = random.randint(2, 5)  # Generate number of values
    key = random.choices(letters_list, k=count_of_values)  # Pick random letters from the list of letters
    random_dict = {i: random.randint(0, 100) for i in key}  # Create random dicts
    result_list.append(random_dict)  # Add all random dicts into the list

print(result_list)  # Check the result of creating random dicts

result_dict = {}  # Initialize empty dict for final results
replacing_dict = {}  # Initialize empty dict for replacing values

# Initialize iteration over list of tuples, with indexes as keys and dicts as values
for dict_index, dict_of_numbers in enumerate(result_list):
    for key in dict_of_numbers.keys():  # Iterate over nested dicts
        if key not in result_dict.keys():  # Check if key is present in result_dict
            result_dict[key] = dict_of_numbers[key]  # Add values from the list if key is not present
        if dict_of_numbers[key] > result_dict[key]:  # Check if key has bigger value than keys from result_dict
            replacing_dict[key] = dict_index  # Write replacing keys to separate dict with indexes as values
            result_dict[key] = dict_of_numbers[key]  # Replace smaller values with bigger one

print(replacing_dict)  # Check the dict with replacing numbers

for old_key, value in replacing_dict.items():  # Iterate over dict of indexes with replacing values
    new_key = f'{old_key}_{value}'  # Create keys renaming
    result_dict[new_key] = result_dict.pop(old_key)  # Delete old key names and add the new one

print(result_dict)  # Check final dict
