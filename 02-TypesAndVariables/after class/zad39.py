# The price of the product on the price tag is given before and after the discount is applied.
# Write a program that allows you to enter the product price and discount. Display the product price,
# discount, discounted product price, and the difference between the product price before and after
# the discount. Display all prices with two decimal places. Sample result:
# Enter price: 24.72 Enter discount %: 15 Price with discount: 21.01 Reduction: 3.71

def main() -> None:
    price = float(input('Enter price:\n'))
    discount = int(input('Enter discount:\n'))

    price_after_discount = round(((100 - discount) * price) / 100, 2)
    reduction = round(price - price_after_discount, 2)

    print(f'Price with discount: {price_after_discount}')
    print(f'Reduction: {reduction}')

if __name__ == '__main__':
    main()