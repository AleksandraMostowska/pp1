# 27.	The grades.txt file contains student’s grades. Create the file in any text editor.
# Name: Peter
# Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
# Then create a program that calculates the arithmetic mean of student’s grades.

import re

def read_grades_from_file(filename: str) -> list[float]:
    with open(filename, 'r') as f:
        # grades_line = [line.strip() for line in f.readlines() if "Grades:" in line]
        # grades_text = grades_line[0].replace("Grades: ", "")
        # grades = [float(grade) for grade in grades_text.split(',')]
        # return grades

        grades = re.findall("\d.\d", f.read())
        return [float(i) for i in grades]

def get_mean(grades: list[float]) -> float:
    if grades:
        mean = sum(grades) / len(grades)
        print("Arithmetic Mean of Grades:", mean)
    else:
        print("No grades found in the file.")

def main() -> None:
    grades = read_grades_from_file('grades.txt')
    print(grades)
    get_mean(grades)

if __name__ == '__main__':
    main()