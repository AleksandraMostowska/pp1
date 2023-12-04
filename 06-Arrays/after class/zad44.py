# 44.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Display array values in rows and columns before and after changes.

import random

def create_2d_array(x: int, y: int) -> list[list[int]]:
    return [[random.randint(1, 10) for _ in range(y)] for _ in range(x)]

def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def swap_first_and_last_col(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
            tmp = arr[i][0] 
            arr[i][0] = arr[i][-1]
            arr[i][-1] = tmp


def main() -> None:
    arr = create_2d_array(3, 5)
    print(arr)
    display(arr)
    print()
    swap_first_and_last_col(arr)
    display(arr)

if __name__ == '__main__':
    main()