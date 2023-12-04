# 35.	The array contains integer numbers from 1 to 999. Write a program that displays 
# elements of the array formatted as below.
# -----------------------------------------
# |   1|  23|   5| 382|   1|  17|   4| 906|
# -----------------------------------------

def main() -> None:
    array = [1, 23, 5, 382, 1, 17, 4, 906]

    numbers = len(array)
    print(('-' * 5 * numbers) + '-')

    for i in range(numbers + 1):
        if i == 0:
            print(f'|{array[i]:4}', end='|')

        elif i == numbers:
            print()
            print(('-' * 5 * numbers) + '-')
        
        else: 
            print(f'{array[i]:4}', end='|')




if __name__ == '__main__':
    main()