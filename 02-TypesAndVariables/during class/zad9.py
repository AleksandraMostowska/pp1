# 9.	Natural values 5, 1, 8, 6, 3 have been assigned to variables named n1, n2, n3, n4, n5. Write a program that calculates and displays:
# a.	sum of all variables
# b.	sum of squared variables
# c.	quotient of the variable three and five
# d.	message (True / False) indicating if the third variable is equal to the fourth variable

def main() -> None:
    n1, n2, n3, n4, n5 = 5, 1, 8, 6, 3
    print(f'Sum: {n1 + n2 + n3 + n4 + n5}')
    print(f'Sum of squared = {n1 ** 2 + n2 ** 2 + n3 ** 2 + n4 ** 2 + n5 ** 2}')
    print(f'Quotient = {n3 / n5}')
    print(f'Are equals = {n3 == n4}')

if __name__ == '__main__':
    main()
