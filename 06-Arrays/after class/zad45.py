# 45.	Create a function identity_matrix(n) that returns an identity matrix of size n 
# (https://en.wikipedia.org/wiki/Identity_matrix). Then create a function that displays a 2D array in rows and columns. 
# Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8.

def identity_matrix(n: int) -> list[list[int]]:
    return [[1 if j == i else 0 for j in range(n)] for i in range(n)]

def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def main() -> None:
    arr = identity_matrix(3)
    display(arr)
    print()
    arr = identity_matrix(5)
    display(arr)
    print()
    arr = identity_matrix(8)
    display(arr)

if __name__ == '__main__':
    main()