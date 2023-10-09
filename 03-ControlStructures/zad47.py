# 47.	Write a program that displays 20 integer random numbers in the range of 5 to 10.

import random

def main() -> None:
    r = 20
    nums = []
    for i in range(20):
        nums.append(random.randint(5, 10))
    
    print(' '.join(map(str, nums)))

if __name__ == '__main__':
    main()