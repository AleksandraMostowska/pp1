# 20.	Write a program that converts any natural number to a binary number. 
# Use the stack. To convert a number, divide the number by 2, each time taking the remainder of the division 
# and putting the remainder on the stack. 
# Repeat the division until the number you are dividing is zero. Then pop and display all values from the stack.

import stack

def convert(number: int) -> None:
    num_left = number
    while num_left > 0:
        stack.push(num_left % 2)
        num_left //= 2
    
    while not stack.empty():
        print(stack.pop())

def main() -> None:
    convert(18)

if __name__ == '__main__':
    main()