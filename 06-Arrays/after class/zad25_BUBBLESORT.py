# 25.	Create a program that sorts elements of an array containing integer numbers. 
# Apply the Bubble Sort sorting algorithm. 
# Define a function bubblesort(array) that returns the sorted array. 
# Try to sort and display any three arrays.

def bubblesort(array: [int]) -> [int]:
    length = len(array) - 1
    sorted = True

    while sorted:
        sorted = False
        for i in range(0, length):
            if array[i] > array[i + 1]:
                sorted = True
                array[i], array[i + 1] = array[i + 1], array[i]
    
    return array

def main() -> None:
    print(bubblesort([12, 5, 3, 8, 10, 2, 6, 8]))

if __name__ == '__main__':
    main()