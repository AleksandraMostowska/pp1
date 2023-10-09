# 22.	Most female names in Polish end with the letter "a". Write a program that displays the name entered 
# from the keyboard, provided it is a female name. Sample result:
# Enter name: Anna
# Anna – Polish female name


def checkIfPolishWomanName() -> None:
    name = input("Enter name: ")
    if name[-1] == "a":
        print(f'{name} – Polish female name')

def main() -> None:
    checkIfPolishWomanName()

if __name__ == '__main__':
    main()