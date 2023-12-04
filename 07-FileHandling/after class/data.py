import re
import json
import csv

def read_from_file(filename: str):
    counter = []
    biggest_avg = 0
    with open(filename, 'r') as f:
        data = json.load(f)
        student_with_biggest_avg = data[0]
        for person in data:
            all_grades = []
            for subject in person["studies"]["courses"]:
                grades = [float(i) for i in subject["grades"]]
                all_grades += grades
            tmp = sum(all_grades) / len(all_grades)
            print(tmp)
            if tmp > biggest_avg:
                biggest_avg = tmp
                student_with_biggest_avg = person
    
    print('-----------------')
    print(biggest_avg)
    print(student_with_biggest_avg)

def main() -> None:
    print(read_from_file('data.json'))

if __name__ == '__main__':
    main()