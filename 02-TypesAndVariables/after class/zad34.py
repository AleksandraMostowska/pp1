# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h.
# Write a program that checks whether the vehicle speed entered from the keyboard
# is correct. Sample result:
# Enter vehicle speed: 158 Speed is valid: False

def main() -> None:
    speed = int(input('Enter vehicle speed: '))
    is_valid = 40 <= speed <= 140

    print(f'Speed is valid: {is_valid}')

if __name__ == '__main__':
    main()