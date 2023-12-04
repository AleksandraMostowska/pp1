import json
import csv

def main() -> None:
    with open("data.json", 'r') as source, open("data2.csv", 'w') as destination:
        json_data = json.load(source)
        headers = json_data[0].keys()
        writer = csv.DictWriter(destination, fieldnames=headers)
        writer.writeheader()
        writer.writerows(json_data)

if __name__ == '__main__':
    main()