# Przepisz ponownie swój program płacowy, używając try i except, tak aby elegancko
# obsługiwał on nienumeryczne dane wejściowe, wyświetlając w takim przypadku wiadomość i kończąc
# swoje działanie. Poniżej znajdują się wyniki dwóch uruchomień programu:
# Podaj liczb ę godzin : 20
# Podaj stawk ę godzinow ą : dziewi ę ć
# B ł ąd , podaj warto ś ć numeryczn ą

def main() -> None:
    try: 
        hours = int(input('Enter hours: '))
        salary = int(input('Enter salary: '))

        if hours <= 40:
            result = hours * salary
        else:
            result = (hours - 40) * (salary * 1.5) + (40 * salary)
        
        print(result)
    
    except:
        raise ValueError('Give numeric value')

if __name__ == '__main__':
    main()