# 28.	The binary numerical system uses two symbols to represent a number: 0 and 1. 
# Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, 
# or False otherwise. Sample result:
# f("101101") returns True
# f("1311a10100") returns False

import bin

def main() -> None:
    print(bin.f('101101'))
    print(bin.f('1311a012'))
    print(bin.f('12345'))
    print(bin.f('abcd'))

if __name__ == '__main__':
    main()