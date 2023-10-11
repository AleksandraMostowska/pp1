# 31.	Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. 
# Sample result:
# f(-7,8) returns 3
# f(-1,11) returns 0

def f(x: int, y: int) -> int:
    return len([i for i in range(x, y) if i < 0 and i % 2 == 0])

def main() -> None:
    print(f(-7, 8))
    print(f(-1, 11))

if __name__ == '__main__':
    main()