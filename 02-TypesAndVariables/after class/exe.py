def main() -> None:
    n = input('Enter credit card number:\n')
    if len(n) != 16:
        raise ValueError('Given number is not correct.')

    print(f'Credit card number: {" ".join([n[i:i+4] for i in range(0, 16, 4)])}')
    

if __name__ == '__main__':
    main()