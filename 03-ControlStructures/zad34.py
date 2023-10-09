# 34.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) 
# read from the keyboard with as few coins as possible.
# Enter the amount in PLN: 18
# The amount of PLN 18 in coins:
# 5 zł – 3 
# 2 zł – 1 
# 1 zł – 1

def get_coin_count() -> int:
    coins = [5, 2, 1]
    amount = int(input('Enter the amount in PLN: '))
    count = 0

    amount_left = amount
    while amount_left != 0:
        if amount_left >= coins[0]:
            count += amount_left // coins[0]
            amount_left %= coins[0]
        if amount_left >= coins[1]:
            count += amount_left // coins[1]
            amount_left %= coins[1]
        if amount_left >= coins[2]:
            count += amount_left // coins[2]
            amount_left %= coins[2]
    
    return count

def main() -> None:
    print(f'The amount of PLN 18 in coins: {get_coin_count()}')

if __name__ == '__main__':
    main()