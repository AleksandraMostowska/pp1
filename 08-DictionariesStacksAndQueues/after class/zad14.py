# 14.	Write a program that spells any text entered from the keyboard, using ICAO spelling alphabet 
# (https://en.wikipedia.org/wiki/NATO_phonetic_alphabet). Create a dictionary where you put all the letters and the corresponding words. 
# Then try to spell your name and three other words. Sample result:
# Enter text: uek
# Spelled text: Uniform Echo Kilo

def spell(word: str) -> str:
    icao_alphabet = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu',
    }

    words = []
    for letter in word:
        if letter.isalpha():
            words.append(icao_alphabet.get(letter.upper(), letter))
        else:
            words.append(letter)
    
    return ' '.join(words)

def main() -> None:
    print(spell('ola'))

if __name__ == '__main__':
    main()