# 25.	Write a program that computes the number of words in the following text. Use regular expressions.
# To be, or not to be, that is the question

import re

def count_words(text: str) -> int:
    # return len(re.findall(r'\b\w+\b', text))
    return len(text.split())

def main() -> None:
    text = 'To be, or not to be, that is the question'
    print(count_words(text))

if __name__ == '__main__':
    main()