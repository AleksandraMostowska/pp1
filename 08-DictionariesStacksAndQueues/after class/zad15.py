# 15.	Write a program that writes to a file ICAO.txt the contents of a dictionary containing ICAO spelling alphabet. Sample file content:
# A Alfa
# B Bravo
# C Charlie
# D Delta
# …
# …
# Z Zulu

def write_icao_to_file(filename: str) -> None:
    icao_alphabet = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu',
    }

    with open(filename, 'w') as f:
        f.write('\n'.join([f'{k} {v}' for k, v in icao_alphabet.items()]))

def main() -> None:
    write_icao_to_file('ICAO.txt')

if __name__ == '__main__':
    main()