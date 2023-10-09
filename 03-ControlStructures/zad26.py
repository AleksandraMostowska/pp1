# 26.	The speed of vehicles on highways in Poland is at least 40 km/h and not more than 140 km/h. 
# Write a program that displays a message when the specified car speed, read from the keyboard, 
# has been exceeded. Sample result:
# Enter car speed: 38
# Warning: invalid car speed!!
# Use the following variables in your program:
# car_speed
# speed_limit_min
# speed_limit_max

def checkIfValidSpeed(speed_limit_min: int, speed_limit_max: int) -> None:
    car_speed = int(input("Enter car speed: "))
    if car_speed < speed_limit_min or car_speed > speed_limit_max:
        print('Warning: invalid car speed!!')


def main() -> None:
    checkIfValidSpeed(40, 140)

if __name__ == '__main__':
    main()