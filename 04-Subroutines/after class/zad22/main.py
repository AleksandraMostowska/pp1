# 22.	Each month of a calendar year can be expressed by its name or by a number that indicates 
# the position of the month in year. In a separate module, define a function month(n) that returns
# a month name based on the month number (values from 1 to 12). Then, create a program to display 
# the name of the month 7. Import the module with the created function. Sample result:
# Enter month number: 9
# The name of month 9 is September

import month

def main() -> None:
    m = int(input("Enter month number: "))
    print(f'The name of month {m} is {month.month(m)}')

if __name__ == '__main__':
    main()