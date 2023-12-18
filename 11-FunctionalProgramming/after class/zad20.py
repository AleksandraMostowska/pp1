# 20.	An array contains numbers from 1 to 20. Write a program that calculates and displays their third power. 
# Use the map() and an anonymous function.

def main() -> None:
    nums = [i for i in range(1, 21)]
    third_powers = list(map(lambda x: x ** 3, nums))
    print(third_powers)

if __name__ == '__main__':
    main()