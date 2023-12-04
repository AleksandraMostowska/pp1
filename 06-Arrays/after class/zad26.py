# 26.	Create a program that displays all unique elements in an array. Sample result:
# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

def main() -> None:
    arr = [2, 3, 2, 5, 8, 1, 9, 8]
    print([i for i in arr if arr.count(i) == 1])

if __name__ == '__main__':
    main()