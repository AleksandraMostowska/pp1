# 44.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
# Entering 0 ends entering numbers. Sample result:
# Enter number: 15
# Enter number: 8
# Enter number: 10
# Enter number: 0
# RESULT: Quantity=3, Sum=33, Mean=11


def main() -> None:
    numbers = []
    while True:
        ip = int(input('Enter number: '))
        if ip == 0:
            break
        numbers.append(ip)
    
    l = len(numbers)
    s = sum(numbers)
    print(f'Quantity: {l}')
    print(f'Sum: {s}')
    print(f'Mean: {s / l}')

if __name__ == '__main__':
    main()