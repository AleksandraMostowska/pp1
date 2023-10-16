# 24.	Write a program that calculates the number of vowels in the text:
# To be, or not to be, that is the question
# Use regular expressions and the findall() method.

import re

def count_vowels(text: str) -> int:
    return len(re.findall(r'[AEOUIYaeouiy]', text))

def main() -> None:
    text = 'To be, or not to be, that is the question'
    print(count_vowels(text))

if __name__ == '__main__':
    main()