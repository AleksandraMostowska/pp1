# 21.	The products.csv file contains data about the products sold. Create the file in a text editor.
# Product,Quantity,Price
# milk,8,4.25
# cheese,5,17.90
# bread,21,6.15
# juice,12,5.90
# Then, write a program to convert data from CSV to JSON. The program reads product data from the CSV file 
# and writes the data to a JSON file.

import csv
import json

def read_from_csv(filename: str) -> dict:
    with open(filename, 'r') as f:
        products = csv.DictReader(f)
        products_data = []
        for v in products:
            products_data.append(v)
    
        return products_data
    
def write_to_json(filename: str, data: dict[str]) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def main() -> None:
    d = read_from_csv('products.csv')
    print(d)
    write_to_json("products.json", d)

if __name__ == '__main__':
    main()