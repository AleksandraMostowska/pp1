# Write a program that enables a user to challenge a computer. The computer throws dice. Then, the user then
# tries to guess the number from dice by entering a number from 1 to 6 from the keyboard. If the user has guessed 
# the number from the dice, the computer displays True. Otherwise, the computer displays False.

import random

def main() -> None:
    number = random.randint(1, 6)

    users_num = int(input('Enter number: '))

    guessed = number == users_num

    print(f'Computer rolled: {number}')
    print(f'Your guess is correct: {guessed}')

if __name__ == '__main__':
    main()