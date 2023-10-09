# 21.	Write a program that displays two numbers entered from the keyboard in ascending order.
# Enter first number: 27
# Enter second number: 14
# Numbers in ascending order: 14, 27

def showInAscendingOrder() -> None:
    t1 = int(input("Enter first number: "))
    t2 = int(input("Enter second number: "))

    nums = sorted([t1, t2])
    print(f'Numbers in ascending order: {nums[0]}, {nums[1]}')

def main() -> None:
    showInAscendingOrder()

if __name__ == '__main__':
    main()