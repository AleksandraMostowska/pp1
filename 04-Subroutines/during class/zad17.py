def different(n1: int, n2: int, n3: int) -> int:
    return n1 != n2 and n2 != n3 and n1 != n3

def main() -> None:
    print(different(1, 2, 3))
    print(different(3, 4, 3))

if __name__ == "__main__":
    main()