# 24.	In a separate module, define a function that checks if the number is within the range <x, y>. 
# The function returns a boolean value. Then, create a program and use the function you defined. 
# Sample result:
# A number: 7
# Number 7 in the range <2,15>: yes 

import check_num

def main() -> None:
    x = 2
    y = 15
    num = 7
    is_in_range = check_num.check_if_in_range(num, x, y)
    print(f"Number {num} in the range: {'yes' if is_in_range else 'no'}")

if __name__ == '__main__':
    main()