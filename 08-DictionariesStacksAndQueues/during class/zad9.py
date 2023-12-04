# 9.	Create an array with 5 dictionaries, each containing a country and its population. Then, using 
# a ‘while’ loop, display the array contents. Sample result:
# countries = [
#     {"name":"Poland", "population":38000000},
#     …
#     …
#     …
#     …
# ]
# COUNTRY  POPULATION
# Poland   38000000
# …        …
# …        …
# …        …
# …        …

def main() -> None:
    countries = [
        {
            "name": "Poland", "population": 38000000
        },
        {
            "name": "France", "population": 67750000
        },
        {
            "name": "Germany", "population": 83200000
        },
        {
            "name": "Portugal", "population": 10330000
        },
        {
            "name": "Spain", "population": 47420000
        },
        {
            "name": "Italy", "population": 59110000
        }
    ]

    print(f'{"COUNTRY":10}{"POPULATION":10}')
    i = 0
    while i != len(countries):
        print(f'{countries[i]["name"]:10}{countries[i]["population"]:<10}')
        i += 1

    print(f'{12345:+>10}')

if __name__ == '__main__':
    main()