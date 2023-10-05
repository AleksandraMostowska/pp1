# Write a program that allows you to enter a binary, four-digit number.
# Convert the entered number from binary to decimal value. Do not use
# available Python functions. Sample result:
# Enter binary number: 0110 Binary number in decimal notation: 6

def main() -> None:
    num = input('Enter 4-digit binary number:\n')
    if len(num) != 4:
        raise ValueError

    num = num[::-1]

    result = 0

    for i in range(len(num)):
        if num[i] == '1':
            result += 2 ** i
    
    print(f'Binary number in decimal notation: {result}')

if __name__ == '__main__':
    main()