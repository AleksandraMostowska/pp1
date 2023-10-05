def main() -> None:
   celcius = int(input('ENter celcius temperature:\n'))
   fahrenheit = celcius * 1.8 + 32
   print(f'Temperature in Fahrenheits: {fahrenheit}')

if __name__ == '__main__':
    main()