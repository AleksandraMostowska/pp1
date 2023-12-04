# 42.	An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. 
# Create a program that finds the smallest and largest values in the array and in which row and column they are located. 

def find_smallest(arr: list[list[int]]) -> list[int]:
    smallest = 100000
    smallestRow = -1
    smallestCol = -1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < smallest:
                smallest = arr[i][j]
                smallestRow, smallestCol = i, j
    
    return [smallest, smallestRow, smallestCol]

def find_biggest(arr: list[list[int]]) -> list[int]:
    biggest = -100000
    biggestRow = -1
    biggestCol = -1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > biggest:
                biggest = arr[i][j]
                biggestRow, biggestCol = i, j
    
    return [biggest, biggestRow, biggestCol]

def flatten(arr: list[list[int]]) -> list[int]:
    return [i for j in arr for i in j]

def main() -> None:
    arr = [[-38, 19], [5,40],[-7,11],[29,16]]

    print(sorted(flatten(arr)))

    smallestItems = find_smallest(arr)
    smallest, smallestRow, smallestCol = smallestItems[0], smallestItems[1], smallestItems[2]
    
    biggestItems = find_biggest(arr)
    biggest, biggestRow, biggestCol = biggestItems[0], biggestItems[1], biggestItems[2]

    print(smallestItems)
    print(biggestItems)

if __name__ == '__main__':
    main()