# An array contains values: [[1,3,5],[8,7,2]]. Write a program that calculates and displays:
# a. Sum of the first element in the first row and the last element in the last row
# b. Sum of the elements in the middle column
# c. Sum of the elements in the last row

def main() -> None:
    arr = [[1,3,5],[8,7,2]]

    print(arr[0][0] + arr[-1][-1])
    print(arr[0][1] + arr[1][1])
    print(sum(arr[1]))

if __name__ == '__main__':
    main()