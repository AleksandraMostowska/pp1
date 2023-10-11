# 46.	Define the function f(x,y), which returns the sum of numbers in the range <x,y> that 
# are completely divisible by 2 and 3 and not divisible by 4. 
# Sample result:
# f(1,20) returns 24
# f(10,30) returns 48

def f(x: int, y: int) -> int:
    return sum([i for i in range(x, y + 1) if i % 6 == 0 and i % 4 != 0])

def main() -> None:
    print(f(1, 20))
    print(f(10, 30))

if __name__ == '__main__':
    main()