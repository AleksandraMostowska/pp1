# 23.	An object representing an employee contains the following data: name, surname, age, and seniority 
# (the number of years worked). Define a C class that allows you to create an object. Provide employee 
# data at the time of creating the object, in the given order. Define a text representation of an object 
# in the class that contains a string of last name, first letter of first name, and seniority. 
# If the employee is an adult (at least 18 years old), use uppercase letters, otherwise lowercase letters. 
# Sample result:
# C("Anna","May",17,7) returns "maya7"
# C("George","Brown",21,4) returns "BROWNG4"

from dataclasses import dataclass

@dataclass
class C:
    name: str
    surname: str
    age: int
    seniority: int

    def is_adult(self):
        return self.age >= 18

    def __str__(self) -> str:
        if self.is_adult():
            return f'{self.surname.upper()}{self.name.upper()[0]}{self.seniority}'
        return f'{self.surname.lower()}{self.name.lower()[0]}{self.seniority}'

def main() -> None:
    c1 = C("Anna","May",17,7)
    print(c1)
    c2 = C("George","Brown",21,4)
    print(c2)

if __name__ == '__main__':
    main()