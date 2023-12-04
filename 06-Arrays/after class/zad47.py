# 47.	Create a function that convert two-dimensional (2D) array into 1D. 
# Then create a program that displays 1D array for the following 2D arrays.
# a.	2 3
#     1 5 

# b.	5 0 3 7 5
#     9 0 9 1 2

# c.	2 1
#     3 5
#     7 4
#     2 6

def flatten(arr: list[list[int]]) -> list[int]:
    return [i for j in arr for i in j]


def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def main() -> None:
    a = [[2, 3], [1, 5]]
    display(a)
    print(flatten(a))
    print()
    b = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
    display(b)
    print(flatten(b))
    print()
    c = [[2, 1], [3, 5], [7, 4], [2, 6]]
    display(c)
    print(flatten(c))

if __name__ == '__main__':
    main()