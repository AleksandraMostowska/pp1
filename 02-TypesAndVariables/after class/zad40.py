# The credit card number consists of 16 digits. Write a program that allows you to enter a credit card
# number from the keyboard. Display the credit card number in groups of 4 digits, separating the groups
# with a space character. Sample result:
# Enter credit card number: 5020312109004442 Card number: 5020 3121 0900 4442

def main() -> None:
    n = input('Enter credit card number:\n')
    if len(n) != 16:
        raise ValueError('Given number is not correct.')
    
    formatted_number = ' '.join([n[i:i+4] for i in range(0, 16, 4)])
    print(f'Credit card number: {formatted_number}')
    

if __name__ == '__main__':
    main()