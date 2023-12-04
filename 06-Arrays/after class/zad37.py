# 37.	Define a function rand_elem(array) that returns a randomly selected array element. 
# Using the function, display a few randomly selected array elements.

import random

def rand_elem(array: [int]) -> int:
    return random.choice(array)

def main() -> None:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in range(5):
        print(rand_elem(arr))

if __name__ == '__main__':
    main()