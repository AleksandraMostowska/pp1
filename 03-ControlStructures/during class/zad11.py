# 11.	Write a program that checks whether the number entered from the keyboard is even or odd. Sample result:
# Enter number: 27
# Number is odd

def main() -> None:
    num = int(input('Enter number: '))

    if num % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')

if __name__ == '__main__':
    main()