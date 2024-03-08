#1
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result:", result)

#2
def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Example usage
string = "Hello World"
upper_count, lower_count = count_case_letters(string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

#3
def is_palindrome(string):
    return string == string[::-1]

# Example usage
string = "radar"
print("Is palindrome?", is_palindrome(string))

#4
import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

# Example usage
number = 25100
delay = 2123
result = square_root_after_delay(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

#5
def all_true(elements):
    return all(elements)

# Example usage
tuple_elements = (True, True, False)
print("All elements true?", all_true(tuple_elements))
