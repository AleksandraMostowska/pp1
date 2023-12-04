# 30.	Define a median(array) function that returns the median of the given array of numbers. 
# Do not use built-in functions. The median is the middle value in the ordered 
# sequence of numbers (https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png). 
# Then, using the defined function, calculate and display the median for the following values:
# a.	[1,0,9,4,6]
# b.	[6,8,3,1,0,5,7]

def median(array: [int]) -> int:
    sorted_numbers = sorted(array)
    print(sorted_numbers)
    n = len(array)

    if n % 2 == 0:
        return int((sorted_numbers[(n - 1) // 2] + sorted_numbers[n // 2]) / 2)
    
    return sorted_numbers[n // 2]

def main() -> None:
    a1 = [1,0,9,4,6]
    a2 = [6,8,3,1,0,5,7]
    print(median(a1))
    print(median(a2))

if __name__ == '__main__':
    main()