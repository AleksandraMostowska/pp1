# 21.	An array contains values: 15, 8, 31, 47, 2, 19. Create a program 
# that calculates and displays the array and the arithmetic mean of array values. 
# Use the “while” loop statement.

def getMean(arr: [int]) -> float:
    # return sum(arr) / len(arr)

    sum = 0.0
    counter = 0
    while counter < len(arr):
        sum += arr[counter]
        counter += 1
    
    return sum / counter

    

def main() -> None:
    arr = [15, 8, 31, 47, 2, 19]

    print("Array:", arr)
    print("Arithmetic Mean:", getMean(arr))

if __name__ == '__main__':
    main()
