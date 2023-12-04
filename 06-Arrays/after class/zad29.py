# 29.	Write a program that displays the difference between the largest and smallest values in 
# an array of integers. Sample result:
# Array: [5,1,9,6,1]
# Result: 8

def main() -> None:
    arr = [5,1,9,6,1]
    print(f'Array: {arr}')

    sorted_arr = sorted(arr)
    print(f'Result: {sorted_arr[-1] - sorted_arr[0]}')

if __name__ == '__main__':
    main()