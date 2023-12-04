# 32.	Create a function minmax(array) that, for the given array of integers, 
# returns a two-element array containing the smallest and largest values in the given array. 
# Sample result:
# Array:  [4,2,8,4,7,9,5]
# Result: [2,9]

def minmax(array: [int]) -> [int]:
    sorted_arr = sorted(array)
    return [sorted_arr[0], sorted_arr[-1]]

def main() -> None:
    arr = [4,2,8,4,7,9,5]
    print(minmax(arr))

if __name__ == '__main__':
    main()