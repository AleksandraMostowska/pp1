# 39.	A sentence is an ordered group of words separated by spaces (spaces). 
# Define a function f(sentence) that returns a sentence with spaces removed. 
# Sample result:
# f("integrated development environment") 
# returns "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing computer programs") 
# returns "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms" 

import re

def f(sentence: str) -> str:
    return re.sub(" ", "", sentence)

def main() -> None:
    print(f("integrated development environment"))
    print(f("A programming language is a system of notation for writing computer programs"))

if __name__ == '__main__':
    main()