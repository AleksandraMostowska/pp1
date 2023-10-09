# 25.	In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. Read the number of purchased products and 
# the product price from the keyboard. Sample result:
# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

def getAmountToPay() -> float:
    number_of_purchased_products = int(input('Enter number of products: '))
    product_price = int(input("Enter price: "))

    to_pay = 0.0

    if number_of_purchased_products > 2:
        discount_price = (75 * product_price) / 100
        to_pay = product_price * 2 + (number_of_purchased_products - 2) * discount_price
    else:
        to_pay = product_price * number_of_purchased_products
    
    return to_pay

def main() -> None:
    print(f'Amount to pay: {getAmountToPay()}')

if __name__ == '__main__':
    main()