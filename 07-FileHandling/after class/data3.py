import json
import csv

def main() -> None:
    with open("data.csv", 'r') as source, open("data2.json", 'w') as destination:
        csv_data = csv.DictReader(source)
        for i in csv_data:
            print(i)
        # data = list(csv_data)
        # json.dump(data, destination, indent=4)

if __name__ == '__main__':
    main()