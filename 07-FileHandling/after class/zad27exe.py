# 27.	The grades.txt file contains student’s grades. Create the file in any text editor.
# Name: Peter
# Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
# Then create a program that calculates the arithmetic mean of student’s grades.

import re

def get_grades(filename: str) -> list[float]:
    grades = []
    with open(filename, 'r') as f:
        # grades_line = [line.strip() for line in f.readlines() if "Grades:" in line]
        # grades = [float(g) for g in re.findall(r'\d\.\d', grades_line[0])]
        # print(grades)
        
        grades = re.findall(r'\d\.\d', f.read())
        print([float(g) for g in grades])
        print(dict([(idx, float(gr)) for idx, gr in enumerate(grades)]))

def main() -> None:
    get_grades('grades.txt')

if __name__ == '__main__':
    main()