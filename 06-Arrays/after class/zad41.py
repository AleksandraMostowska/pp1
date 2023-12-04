# 41.	An array contains values: [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]. 
# Create a program that modifies the array values to create a multiplication table as below. Use loop statements. 
# Display the array.
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

def create_2d_array(x: int, y: int) -> list[list[int]]:
    return [[0] * y  for _ in range(x)]

def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def fill_arr_with_products(arr: list[list[int]]) -> list[list[int]]:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = (i + 1) * (j + 1)
    
    return arr


def main() -> None:
    arr = create_2d_array(5, 5)
    display(arr)
    display(fill_arr_with_products(arr))

if __name__ == '__main__':
    main()