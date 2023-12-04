# The binary system uses two symbols to represent a number: 0 and 1.
# Define a function f(binary_number) that returns True if the given notation is a valid binary number, 
# or false otherwise. 

import re

def f(binary_number: str) -> bool:
    return len(re.sub("[^10]", "", binary_number)) == len(binary_number)

