# 34.	Define the function f(n), which returns numbers from 1 to n as a string. Sample result:
# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n: int) -> str:
    return ''.join([str(i) for i in range(1, n + 1)])

def main() -> None:
    print(f(11))
    print(f(4))

if __name__ == '__main__':
    main()