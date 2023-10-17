# Przepisz ponownie swój program obliczający wynagrodzenie, tak aby dać pracownikowi
# 1,5 raza większą stawkę godzinową za czas przepracowany powyżej 40 godzin.
# Podaj liczb ę godzin : 45
# Podaj stawk ę godzinow ą : 10
# Wynagrodzenie : 475.0

def main() -> None:
    hours = int(input('Enter hours: '))
    salary = int(input('Enter salary: '))

    if hours <= 40:
        result = hours * salary
    else:
        result = (hours - 40) * (salary * 1.5) + (40 * salary)
    
    print(result)

if __name__ == '__main__':
    main()