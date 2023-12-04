# 11.	Create a dictionary that describes your favorite book or movie with at least five key-value pairs. 
# Then, create a program that writes the dictionary data to the favourite.json file. Use the dump() method. 
# Pay attention to the formatting of the data in the json file. Use the 'indent' parameter in the dump() method. 
# Sample result:
# movie = {
#     "title":"…",
#     "year": …,
#     "actor":{"leading":"…","supporting":"…"},
#     "oscar":False,
#     …
#     …
#     …
# }

import json

def write_to_json(filename: str, data: dict[str]) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main() -> None:
    movie = {
        "title": "abc",
        "year": "1970",
        "actor": {"leading": "xyz", "supporting": "defg"},
        "oscar": True,
        "languages": ["Polish", "English", "French"]
    }

    for k, v in movie.items():
        print(f'{k}: {v}')

    write_to_json("favourite.json", movie)

if __name__ == '__main__':
    main()