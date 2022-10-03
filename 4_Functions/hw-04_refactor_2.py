"""
Refactoring for homework 2
"""

import random  # Import random module for numbers generation
import string  # Import string module for letters generator

random.seed(a=4)  # Use the same set of random numbers between executions (for debug purpose)


def generate_list_of_dicts(min_values: int,
                           max_values: int,
                           min_range=2,
                           max_range=10,
                           min_dicts=1,
                           max_dicts=100) -> list:
    """create a list of random number of dicts"""
    initial_list = []  # Initialize empty list for random dicts
    for i in range(random.randint(min_range, max_range)):  # Initialize iteration in random range
        letters_list = string.ascii_lowercase  # Generate list of letters
        count_of_values = random.randint(min_values, max_values)  # Generate number of values
        keys = random.choices(letters_list, k=count_of_values)  # Pick random letters from the list of letters
        random_dict = {i: random.randint(min_dicts, max_dicts) for i in keys}  # Create random dicts
        initial_list.append(random_dict)  # Add all random dicts into the list
    return initial_list


result_list = generate_list_of_dicts(2, 5)
print(result_list)  # Call function with list of dicts as a result


def generate_dict_with_biggest_values(input_list: list) -> dict:
    """get previously generated list of dicts and create one common dict:
    if dicts have same key, it will take max value, and rename key with dict number with max value
    if key is only in one dict - it'll take it as is"""
    result_dict = {}  # Initialize empty dict for final results
    replacing_dict = {}  # Initialize empty dict for replacing values
    # Initialize iteration over list of tuples, with indexes as keys and dicts as values
    for dict_index, dict_of_numbers in enumerate(input_list):
        for key in dict_of_numbers.keys():  # Iterate over nested dicts
            if key not in result_dict.keys():  # Check if key is present in result_dict
                result_dict[key] = dict_of_numbers[key]  # Add values from the list if key is not present
            if dict_of_numbers[key] > result_dict[key]:  # Check if key has bigger value than keys from result_dict
                replacing_dict[key] = dict_index  # Write replacing keys to separate dict with indexes as values
                result_dict[key] = dict_of_numbers[key]  # Replace smaller values with bigger one
    for old_key, value in replacing_dict.items():  # Iterate over dict of indexes with replacing values
        new_key = f'{old_key}_{value}'  # Create keys renaming
        result_dict[new_key] = result_dict.pop(old_key)  # Delete old key names and add the new one
    return result_dict


final_results = generate_dict_with_biggest_values(result_list)
print(final_results)  # Call function with final results
