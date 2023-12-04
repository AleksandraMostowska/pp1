# A two-dimensional array contains the following numbers:
# 7 3 7 9 0
# 2 9 0 1 5
# 3 8 6 4 7
# 8 7 1 1 5
# Create a program that calculates the sum of values in the last column.

def sumValuesInColumn(arr: list[list[int]]) -> int:
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][len(arr[i]) - 1]
    
    return sum

def main() -> None:
    arr = [
        [7, 3, 7, 9, 0],
        [2, 9, 0, 1, 5],
        [3, 8, 6, 4, 7],
        [8, 7, 1, 1, 5]
    ]

    print(sumValuesInColumn(arr))

if __name__ == '__main__':
    main()