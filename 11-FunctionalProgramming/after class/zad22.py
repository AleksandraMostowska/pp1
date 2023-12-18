# 22.	The array below contains employee data: 
# [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
#  ("Jackson","Peter"),("Johnson","Rick"),
#  ("Lewis","Terry"),("Clarke","Robin")]
# Write a program that determines and displays a list of employees whose last names are given 
# in capital letters followed by first names, separated by commas. Sample result:
# SMITH, Lucy
# JONES, Janet
# …
# …

def main() -> None:
    employee_data = [
        ("Smith", "Lucy"),
        ("Jones", "Janet"),
        ("Lee", "Jerry"),
        ("Jackson", "Peter"),
        ("Johnson", "Rick"),
        ("Lewis", "Terry"),
        ("Clarke", "Robin") 
    ]

    for last_name, first_name in employee_data:
        formatted_name = f"{last_name.upper()}, {first_name}"
        print(formatted_name)


if __name__ == '__main__':
    main()