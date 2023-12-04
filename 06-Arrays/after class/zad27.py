# 27.	Define a function occurs(number, array) that returns True if a given number is present in an array. 
# Then create a program that checks whether the number entered from the keyboard is present in 
# the array [15, 38, 7, 23, 14]. Sample result:
# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the array

def occurs(number: int, arr: [int]) -> bool:
    # if number not in arr:
    #     return False
    # return True
    return True if number in arr else False

def main() -> None:
    arr = [15, 38, 7, 23, 14]
    n = int(input('Enter number: '))
    print(f'Number: {n}')
    print(f'Array: {arr}')
    print(f"Result: number {n} {'appears in the array' if occurs(n, arr) else  'does not appear in the array'}")

if __name__ == '__main__':
    main()