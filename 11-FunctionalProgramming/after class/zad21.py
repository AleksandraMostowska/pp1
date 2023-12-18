# 21.	An array contains numbers from 1 to 20. Write a program that displays only numbers divisible by 2 and 3 without remainder. 
# Use the filter() and an anonymous function.

def main() -> None:
    nums = [i for i in range(1, 21)]
    third_powers = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, nums))
    print(third_powers)

if __name__ == '__main__':
    main()