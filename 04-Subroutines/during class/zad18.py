def numbers(n: int) -> str:
    return ' '.join([str(i) for i in range(1, n + 1)])

def main() -> None:
    print(numbers(15))
    print(numbers(7))

if __name__ == "__main__":
    main()