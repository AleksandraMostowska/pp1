# 34.	Define a function that returns the elements of the array as a string, 
# separated by commas. Using defined functions, display the contents of any array. 
# Sample result:
# Array: [5,4,3,2,6,5]
# String: 5,4,3,2,6,5

def array_to_text(arr: [int]) -> str:
    return ','.join([str(i) for i in arr])

def main() -> None:
    arr = [5,4,3,2,6,5]
    print(array_to_text(arr))

if __name__ == '__main__':
    main()