# 10.	Write a program to calculate the absolute value of a number entered from the keyboard. Sample result:
# Enter number: -17
# |-17| = 17


def main() -> None:
    num = int(input('Enter num: '))
    if num >= 0:
        print(num)
    else:
        print(-num)

if __name__ == '__main__':
    main()