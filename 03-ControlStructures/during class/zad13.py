# 13.	A user enters two integer numbers from the keyboard. Write a program that checks whether at least one of them is not negative. Sample result:
# Enter number 1: 25
# Enter number 2: -17
# At least one of entered numbers 25 and -17 is not negative

def main() -> None:
    n1 = int(input('Enter number 1: '))
    n2 = int(input('Enter number 2: '))

    if n1 >= 0 or n2 >= 0:
        print(f'At least one of entered numbers {n1} and {n2} is not negative')
    else:
        print(f'Both numbers {n1} and {n2} are negative')

if __name__ == '__main__':
    main()