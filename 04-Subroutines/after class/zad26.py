# 26.	Define an anonymous function that returns True when a number is even or False otherwise.

def main() -> None:
    fun = lambda x: True if x % 2 == 0 else False

    print(fun(8))
    print(fun(7))

if __name__ == '__main__':
    main()