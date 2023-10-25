def read_number() -> int:
    try:
        return int(input('Enter a number: '))
    except:
        raise ValueError('Wrong input type')

def main() -> None:
    print(read_number())

if __name__ == "__main__":
    main()