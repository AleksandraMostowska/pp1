# 26.	Find any text file on the Internet and download it to your computer. 
# Then write a program that displays all words with at least six letters from the file. 
# Display each word on a separate line. Use regular expressions.

import re

def display_six_and_more_letters_words(filename: str) -> None:
    words = []
    with open(filename, "r") as f:
        print(re.findall(r'[A-Za-z]{6,}', f.read()))

        # for line in f.readlines():
        #     if re.match(r'^[A-Za-z]{6,}$', line):
        #         print(line, end='')

def main() -> None:
    display_six_and_more_letters_words('filename.txt')

if __name__ == '__main__':
    main()