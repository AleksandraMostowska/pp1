def main() -> None:
    # a. Length of the phrase: "computer science"
    phrase = "computer science"
    length = len(phrase)
    print(f"a. Length of the phrase: {length}")

    # b. Letter read from the keyboard
    letter = input("b. Enter a letter: ")
    print(f"You entered the letter: {letter}")

    # c. String representing the number 5068
    number_str = "5068"
    print(f"c. String representing the number 5068: {number_str}")

    # d. Numeric representing the string "20303"
    string_num = "20303"
    numeric_num = int(string_num)
    print(f"d. Numeric representing the string '20303': {numeric_num}")

    # e. The smallest number given: 4,7,2,3,9,8
    numbers = [4, 7, 2, 3, 9, 8]
    smallest_number = min(numbers)
    print(f"e. The smallest number among {numbers}: {smallest_number}")

if __name__ == '__main__':
    main()