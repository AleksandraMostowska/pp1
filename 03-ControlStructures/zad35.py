# 35.	Write a program that displays numbers from 1 to 30. If the number is divisible by 3 then the program 
# displays the word 'THREE'. Next, if the number is divisible by 5 then the program displays the word 'FIVE'. 
# Finally, if the number is divisible by both 3 and 5 then the program displays the word 'BINGO'. Sample result:
# 1 2 THREE 4 FIVE THREE 7 ...

def display() -> None:
    range_max = 30
    range_min = 1
    result = ''

    for i in range(range_min, range_max + 1):
        if i % 15 == 0:
            result += 'BINGO '
        elif i % 3 == 0:
            result += 'THREE '
        elif i % 5 == 0:
            result += 'FIVE '
        else:
            result += str(i) + " "
    
    print(result)

def main() -> None:
    display()

if __name__ == '__main__':
    main()
        