# 15.	Write a program that reads temperature in degrees Celsius from the keyboard. 
# Then, the program calculates and displays the temperature in Kelvin and Fahrenheit. 
# Use comments to briefly describe the program's algorithm.

def main() -> None:
    celcius = int(input("Enter temperature in Celcius: "))
    kelvin = 273.15 + celcius
    fahrenheit = celcius * 9/5 + 32
    print(f'Temperature in Kelvins: {kelvin}')
    print(f'Temperature in Fahrenheits: {fahrenheit}')

if __name__ == '__main__':
    main()