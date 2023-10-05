# Write a program that checks whether the number entered from the keyboard is even. Display True when the number
# is even and False when the number is odd.
# Sample result:
# Enter number: 34 Number is even: True

def main() -> None:
    n = int(input('Enter number: '))
    is_even = n % 2 == 0

    print(f'Number is even: {is_even}')

if __name__ == '__main__':
    main()