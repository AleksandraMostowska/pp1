# 43.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last row. Display array values 
# in rows and columns before and after changes.

import random

def create_2d_array(x: int, y: int) -> list[list[int]]:
    return [[random.randint(1, 10) for _ in range(y)] for _ in range(x)]

def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def swap_first_and_last_row(arr: list[list[int]]) -> None:
    tmp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = tmp


def main() -> None:
    arr = create_2d_array(3, 5)
    print(arr)
    display(arr)
    print()
    swap_first_and_last_row(arr)
    display(arr)

if __name__ == '__main__':
    main()