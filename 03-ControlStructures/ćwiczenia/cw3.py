# Napisz program, który poprosi użytkownika o wartość pomiędzy 0.0 a 1.0. Jeśli wartość
# jest poza zakresem, wypisz komunikat o błędzie. Jeśli wartość jest między 0.0 a 1.0, wypisz ocenę,
# korzystając z poniższej tabeli:
# Warto ś ć Ocena
# >= 0.9 5 ,0
# >= 0.8 4 ,5
# >= 0.7 4 ,0
# >= 0.6 3 ,5
# >= 0.5 3 ,0
# < 0.5 2 ,0

def get_grade() -> float:
    try:
        number = float(input('Enter number between 0.0 and 1.0: '))
        print(number)

        if number < 0.0 or number > 1.0:
            raise ValueError('Given value is not in correct range')
        
        if number < 0.5:
            grade = 2.0
        elif number < 0.6:
            grade = 3.0
        elif number < 0.7:
            grade = 3.5
        elif number < 0.8:
            grade = 4.0
        elif number < 0.9:
            grade = 4.5
        else:
            grade = 5.0
        
        return grade
    
    except:
        raise ValueError('Given value must be numeric')

def main() -> None:
    print(get_grade())

if __name__ == '__main__':
    main()