# 17.	Write a program that calculates the sum of integer numbers in the range <1,5>. Use the "while" statement.

def main() -> None:
    i = 1
    sum = 0
    while i <= 5:
        sum += i
        i += 1
    
    print(sum)

if __name__ == '__main__':
    main()