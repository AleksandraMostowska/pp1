# 52.	Define a function power(x, n) that calculates xn. Apply recursion. 
# Then, calculate 53.
# Tip: xn =  x * xn-1

def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n > 1:
        return x * power(x, n - 1)

def main() -> None:
    print(power(5, 3))
    print(power(2, 16))

if __name__ == '__main__':
    main()