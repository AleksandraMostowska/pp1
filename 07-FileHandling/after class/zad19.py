# 19.	Create a program that writes to a text file integer numbers in the range of <1,50>, every number in a separate line.

def write_numbers(filename: str) -> None:
    with open(filename, 'w') as f:
        f.write('\n'.join([str(i) for i in range(1, 51)]))

def main() -> None:
    write_numbers('numbers_in_range.txt')

if __name__ == '__main__':
    main()