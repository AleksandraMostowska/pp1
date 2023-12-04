# 12.	Write a program in which you create a dictionary containing student data. 
# Try to describe a student in detail, using different data types that can be used in the dictionary. 
# Then, save the data about student in the file student.json, in a readable form.

import json

def write_to_file(filename: str, data: dict[str]) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main() -> None:
    student = {
        "name": "Alojzy",
        "surname": "Mucha",
        "age": 20,
        "studies": "applied informatics",
        "year": 1,
        "semester": 1,
        "subjects": ["Programming", "Math", "EDI"],
        "is_still_student": True,
        "teachers": {"Programming": "abc", "Math": "defg", "EDI": "xyz"} 
    }

    for k, v in student.items():
        print(f'{k}: {v}')
    
    write_to_file("student.json", student)


if __name__ == "__main__":
    main()