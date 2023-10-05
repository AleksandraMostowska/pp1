# 23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. 
# Then, it calculates and displays both the amount and its VAT. Apply formatting with two decimal
#  places. Sample result:
# Amount : 15.84 VAT 23% : 3.64

def main() -> None:
    amount = float(input('Enter amount: '))
    vat = 0.23 * amount

    print(f'Amount: {amount:.2f}')
    print(f'VAT 23%: {vat:.2f}')

if __name__ == '__main__':
    main()
