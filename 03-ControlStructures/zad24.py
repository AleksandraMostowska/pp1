# 24.	A computer program analyses the price of a product in an online store.
# If the product price decreases by at least 10%, the program displays a purchase recommendation:
# Buy the product!!
# Product price reduced by 17%

def main() -> None:
    original_price = 200
    new_price = 140

    discount = 100 - ((new_price * 100) / original_price)
    if discount >= 10:
        print('Buy the product!!')
        print(f'Product price reduced by {discount}%')

if __name__ == '__main__':
    main()