def main() -> None:
    hours = int(input('Podaj liczbe godzin:\n'))
    salary = float(input('Podaj stawke godzinowa:\n'))
    print(f'Wynagrodzenie: {hours * salary}')
    

if __name__ == '__main__':
    main()