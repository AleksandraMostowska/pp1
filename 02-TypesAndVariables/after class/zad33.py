# The password is valid if it is at least 8 characters long. Write a program that checks whether the password
# read from the keyboard is correct. Sample result:
# Enter password: qwertyXX Password is valid: True

def main() -> None:
    password = input('Enter password: ')
    is_valid = len(password) >= 8

    print(f'Password is valid: {is_valid}')

if __name__ == '__main__':
    main()