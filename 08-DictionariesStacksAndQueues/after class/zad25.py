# 1.	The program contains two dictionaries with personal data:
# basic_data = {
#     "name":"Barbara",
#     "age":21
# }

# advanced_data = {
#     "status":"student",
#     "married":False,
#     "interest":["reading","swimming"]
# }
# Write a program that creates a dictionary called ‘person’ containing data from 
# the two given dictionaries (five key-value pairs). Display the contents of the ‘person’ dictionary.

def merge(d1: dict, d2: dict) -> dict:
    person = {} 
    person.update(d1)
    person.update(d2)
    return person

def main() -> None:
    d1 = {
        "name":"Barbara",
        "age":21
    }

    d2 = {
        "status":"student",
        "married":False,
        "interest":["reading","swimming"]
    }


    print(merge(d1, d2))

if __name__ == '__main__':
    main()