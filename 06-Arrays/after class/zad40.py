# 40.	A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0.
# Create a program and the function. 
# Then create a two-dimensional array with dimensions of 3 by 5. Display the created array.

def create_2d_array(x: int, y: int) -> list[list[int]]:
    return [[0] * y  for _ in range(x)]

def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def main() -> None:
    arr = create_2d_array(3, 5)
    print(arr)
    display(arr)

if __name__ == '__main__':
    main()