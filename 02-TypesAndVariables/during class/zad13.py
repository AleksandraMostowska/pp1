# 13.	Write a program that calculates the surface area of a cube. Read the length of the side of the cube from the keyboard. 
# Take into account that the input() function returns a string, not a number. To convert a string to a number, use the int() function. 
# Sample result:
# Enter cube side: 6
# The surface area of a cube with side 6 is 216

def main() -> None:
    cube_side = int(input('Enter cube side: '))
    area = cube_side ** 2 * 6
    print(f'The surface area of cube with side {cube_side} is {area}')

if __name__ == '__main__':
    main()