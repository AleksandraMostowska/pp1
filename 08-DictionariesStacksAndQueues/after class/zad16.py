# 16.	Using the website https://mockaroo.com, generate a list of 500 students, containing the following data: 
# name, surname, student ID, gender, age, year of study, email. Write the data to the students.json file. 
# Then write a program that creates a limited.json file with the copy of the list of students, limited to data: first name, last name, student id.

import json

def create_limited_copy(source: str, destination: str) -> None:
    with open(source, 'r') as s_file:
        people_data = json.load(s_file)
        limited_data = []
        
        for person in people_data:
            limited_student = {
                "first name:": person["name"],
                "last name": person["surname"],
                "student id": person["id"]
            }
            limited_data.append(limited_student)
    

    with open(destination, 'w') as d_file:
        json.dump(limited_data, d_file, indent=4)
        

def main() -> None:
    create_limited_copy('students.json', 'limited.json')

if __name__ == '__main__':
    main()