# Vehicle registration numbers in Kraków start with the letters KR or KK. Write a program that
#  checks whether the vehicle registration number entered from the keyboard means a vehicle from
#  Krakow. Display True whether a car is from Kraków or False otherwise. Sample result:
# Enter vehicle registration number: KR45091 Car from Kraków: True

def main() -> None:
    num = input('Enter vehicle number: ')

    is_from_cracow = num[:2] == 'KK' or num[:2] == 'KR'

    print(f'Car from Kraków: {is_from_cracow}')

if __name__ == '__main__':
    main()