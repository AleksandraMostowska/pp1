# 20.	Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate line.

import random

def write_numbers(filename: str) -> None:
    with open(filename, 'w') as f:
        f.write('\n'.join([str(random.randint(100, 999)) for _ in range(50)]))

def main() -> None:
    write_numbers('random_numbers.txt')

if __name__ == '__main__':
    main()