"""
create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console
"""

# Import random module for numbers generation
import random

random_list = []  # Initialize empty list for random numbers
for i in range(100):  # Initialize iteration over a sequence of numbers from 0 to 100
    random_list.append(random.randint(0, 1000))  # Add random numbers from 0 to 1000 to empty list

random_list = [random.randint(0, 1000) for i in range(100)]  # Optional list comprehension solution

print(random_list)  # Check the results of numbers generation

# Iterate over list indexes
for initial_index in range(len(random_list)):
    # Iterate over next list items
    for secondary_index in range(initial_index + 1, len(random_list)):
        # Swap items for ascending sorting
        if random_list[initial_index] > random_list[secondary_index]:
            random_list[initial_index], random_list[secondary_index] = random_list[secondary_index], random_list[
                initial_index]

print(random_list)  # Check the results of numbers sorting

# Create empty lists for odd and even numbers
even_list = []
odd_list = []
# Iterate over the list of random numbers to find even and odd numbers
for i in random_list:
    if i % 2 == 0:
        even_list.append(i)  # Add even numbers into even_list
    elif i % 2 == 1:
        odd_list.append(i)  # Add odd numbers into odd_list

# Calculate average for even numbers
avg_even = int(sum(even_list) / len(even_list))
# Printing results for even numbers
print(f'Average for even numbers is {avg_even}')

# Calculate average for odd numbers
avg_odd = int(sum(odd_list) / len(odd_list))
# Printing results for odd numbers
print(f'Average for odd numbers is {avg_odd}')
