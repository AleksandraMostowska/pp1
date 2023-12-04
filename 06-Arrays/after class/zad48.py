# An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. 
# Create a program that displays the longest name (consisting of the largest number of characters). 
# Sample result: Names: Genowefa Onufry Celestyna Alojzy Pankracy Longest name: Celestyna

def get_longest(names: list[str]) -> str:
    return max(names, key=len)

def main() -> None:
    Names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
    print(get_longest(Names))

if __name__ == '__main__':
    main()