# 29.	The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns 
# the minimum number of coins that can be used to pay for the purchased product. Sample result:
# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

def f(price: int) -> int:
    counter = 0

    if price >= 5:
        counter += price // 5
        price %= 5
        
    if price >= 2:
        counter += price // 2
        price %= 2
        
    if price >= 1:
        counter += price // 1
        price %= 1
    
    return counter

def main() -> None:
    print(f(23))
    print(f(8))
    print(f(0))

if __name__ == '__main__':
    main()