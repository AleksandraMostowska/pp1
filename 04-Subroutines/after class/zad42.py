# 42.	Define the function f(number1,number2,number3), which returns the difference between the largest 
# and smallest numbers. 
# Sample result:
# f(7,4,9) returns 5
# f(2,12,8) returns 10

def f(n1: int, n2: int, n3: int) -> int:
    return max(n1, n2, n3) - min(n1, n2, n3)

def main() -> None:
    print(f(7, 4, 9))
    print(f(2, 12, 8))

if __name__ == '__main__':
    main()