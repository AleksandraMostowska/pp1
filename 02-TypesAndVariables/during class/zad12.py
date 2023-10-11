# 12.	Write a program that reads your name and surname from the keyboard. 
# Store this data in two separate variables. Then, display your first and 
# last name separated by a single space. Sample result:
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last surname: ')
# full_name = first_name + ' ' + last_name
# print(f'Your fullname is {full_name}')


def main() -> None:
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last surname: ')
    full_name = first_name + ' ' + last_name
    print(f'Your fullname is {full_name}')

if __name__ == '__main__':
    main()