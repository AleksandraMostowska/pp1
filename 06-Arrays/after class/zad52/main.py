# A variable contains text:
# An apple a day keeps the doctor away
# Create a module MyText, containing:
# a. A function that returns the number of words in the text
# b. A function that returns an ordered array of words, from longest to shortest
# c. A function that returns an alphabetically ordered array of words
# Then, write a program, call the functions and display results. Sample result:
# Text: An apple a day keeps the doctor away Number of words: 8 Words from the longest: doctor,apple,… 
# Words ordered alphabetically: a,An,apple,away,…

import myText as mt

def main() -> None:
    t = "An apple a day keeps the doctor away"

    print(mt.number_of_words(t))
    print(mt.sorted_words(t))
    print(mt.sort_alphabetically(t))

if __name__ == '__main__':
    main()