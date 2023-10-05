# The employee file contains the employee's data in a descriptive form. Write a program in which the personal
# _data variable contains employee data:
# "Mr. John May, born on 1998-02-16"
# Display the employee's name, surname, initials and date of birth on separate lines. Sample result:
# Description: Mr. John May, born on 1998-02-16 Name: John Surname: May Initials: JM Born: 1998-02-16

def main() -> None:
    personal_data = "Mr. John May, born on 1998-02-16"
    print(f'Description: {personal_data} Name: {personal_data[4:8]} Surname: {personal_data[9:12]} Initials: {personal_data[4]}{personal_data[9]} Born: {personal_data[22:]}')

if __name__ == '__main__':
    main()