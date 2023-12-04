# 7.	Create a dictionary as in the example below. Note the structure of the dictionary (key-value) 
# and the value types in the example below. What type of value was used in each of the six key-value pairs?
# person = {
#     "name": "Marek",
#     "surname": "Banach",
#     "age": 25,
#     "hobby": ["swimming","excursions"],
#     "married": True,
#     "phone":{"landline":"123444321","mobile":"777888999"}
#    }
# Then, create a program that:
# a.	Displays contents of the dictionary
# b.	Displays name
# c.	Displays hobby
# d.	Changes surname to 'Nowak'
# e.	Changes person's marriage status
# f.	Adds gender: 'male'
# g.	Adds a new hobby: 'bicycle'
# h.	Adds work phone to existing phones: '313131444'

def main() -> None:
    person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
    
    for k, v in person.items():
        print(f'{k}: {v}')
    
    print(person["name"])
    print(person["hobby"])
    person["surname"] = "Nowak"
    print(person["surname"])
    person["married"] = False
    print(person["married"])
    person["gender"] = "male"
    person["hobby"].append("bicycle")
    print(person["hobby"])
    person["phone"].update({"work": '313131444'})
    print(person["phone"])

if __name__ == '__main__':
    main()