import random

def f(n: int) -> int:
    if n <= 5:
        return n * 100
    if n <= 8:
        return 500 + (n - 5) * 200
    return 1100 + (n - 8) * 50


def main() -> None:
    print(f(7))

if __name__ == '__main__':
    main()