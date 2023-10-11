# 33.	Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:
# f(4) returns "*/*/*/*"
# f(1) returns "*"

def f(n: int) -> str:
    return '/'.join(['*' for _ in range(n)])

def main() -> None:
    print(f(4))
    print(f(1))

if __name__ == '__main__':
    main()