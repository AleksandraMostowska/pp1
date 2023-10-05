# To improve readability, telephone numbers are often presented with a dash or space separating some digits.
#  Write a program that displays a 9-digit telephone number entered from the keyboard as three groups
#  of 3 digits each, separated by a dash character. Sample result:
# Enter phone number: 543097329 Phone number: 543-097-329

def main() -> None:
    number = input('Enter number:\n')
    formatted = '-'.join([number[i:i+3] for i in range(0, 9, 3)])

    print(f'Phone number: {formatted}')

if __name__ == '__main__':
    main()