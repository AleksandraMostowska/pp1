# 8.	Create a dictionary describing your mobile phone. Use at least 6 key-value pairs of data of different types. 
# Then, using 'for' loop, display the contents of the dictionary. To read a key and value, use the items() method. 
# Sample result:
# mobile = {
#     "OS":"Android",
#     …
#     …
#     …
#     …
#     …
# }
# for key,value in mobile.items():
#     print(f"{key} : {…}")

def main() -> None:
    mobile = {
        "OS": "ios",
        "color": "white",
        "model": 11,
        "year": 2020,
        "GB": 64,
        "mark": "Apple"     
    }

    for k, v in mobile.items():
        print(f'{k}: {v}')

if __name__ == '__main__':
    main()