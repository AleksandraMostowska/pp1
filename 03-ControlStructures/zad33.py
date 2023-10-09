# 33.	Write a program that converts a decimal number into a binary number. To convert a decimal number to binary, 
# follow these steps:
# a.	Read a decimal number from the keyboard.
# b.	Divide the number by 2 and note the remainder.
# c.	Divide the quotient obtained by 2 and note the remainder.
# d.	Repeat the same process till we get 0 as the quotient.
# e.	Write the values of all the remainders starting from the bottom to the top. That will be the required 
# binary number.
# Sample result:
# Enter decimal number: 12
# 12(10) = 1100(2)

def bin_to_dec() -> None:
    num = input('Enter number: ')
    tmp = num
    num = num[::-1]
    result = 0
    for i in range(len(num)):
        if num[i] == '1':
            result += 2 ** i
    
    print(f"{tmp}(2) = {result}(10)")

def dec_to_bin() -> None:
    dec = input('Enter number: ')
    binary_num = ''
    quotient = int(dec)

    while quotient > 0:
        reminder = quotient % 2
        binary_num += str(reminder)
        quotient //= 2
    
    binary_num = binary_num[::-1]
    print(f"{dec}(10) = {binary_num}(2)")

def main() -> None:
    # bin_to_dec()
    dec_to_bin()

if __name__ == '__main__':
    main()