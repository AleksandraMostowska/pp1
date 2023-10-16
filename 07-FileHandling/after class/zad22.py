# 22.	In any text editor, create a text file students.txt containing the following data in CSV format:
# first_name,last_name,age,gender,email
# Decca,Blackstone,52,Male,dblackstone0@time.com
# Elena,Rechert,27,Female,erechert1@ucoz.com
# Bibbye,Norree,26,Female,bnorree2@reddit.com
# Alasdair,McCoole,53,Male,amccoole3@foxnews.com
# Hogan,Hatrey,26,Male,hhatrey4@zimbio.com
# Then create a program that reads data from the CSV file and displays the first name, last name and email address of students under 30. Format the data as below. Sample result:
# Elena   Rechert  erechert1@ucoz.com
# Bibbye  Norree   bnorree2@reddit.com
# Hogan   Hatrey   hhatrey4@zimbio.com

import csv

def read_from_file(filename: str) -> None:
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        
        for person in reader:
            if int(person['age']) <= 30:
                print(f"{person['first_name']:<8} {person['last_name']:<9} {person['email']}")

def main() -> None:
    read_from_file('students.txt')

if __name__ == '__main__':
    main()
