# A bank buys and sells Euro. Write a program that, based on the Euro buying and selling rates entered
# from the keyboard, calculates the difference between the buying and selling rates (spread).
# Display result with 4 decimal places. Sample result:
# Bank buys EUR: 4.5940 Bank sells EUR: 4.6250 Spread: 0.0310

def main() -> None:
    buy_rate = float(input('Enter Euro buying rate: '))
    sell_rate = float(input('Enter Euro selling rate: '))

    spread = sell_rate - buy_rate

    print(f'Bank buys EUR: {buy_rate:.4f}')
    print(f'Bank sells EUR: {sell_rate:.4f}')
    print(f'Spread: {spread:.4f}')

if __name__ == '__main__':
    main()
