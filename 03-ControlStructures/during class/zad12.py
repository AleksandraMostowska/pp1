# 12.	Paul is 21 and Annie is 18. Write a program that checks that two people are adults. Sample result:
# Enter first person name: Peter
# Enter first person age: 21
# Enter second person name: Ann
# Enter second person age: 18
# Both Peter and Ann are adults

def is_adult(age: int) -> bool:
    return age >= 18

def main() -> None:
    p1_name = input('Enter first person name: ')
    p1_age = int(input('Enter first person age: '))
    is_p1_adult = is_adult(p1_age)

    p2_name = input('Enter second person name: ')
    p2_age = int(input('Enter second person age: '))
    is_p2_adult = is_adult(p2_age)

    if is_p1_adult and is_p2_adult:
        print(f'Both {p1_name} and {p2_name} are adults')
    elif not is_p1_adult and not is_p2_adult:
        print(f'Both {p1_name} and {p2_name} are not adults')
    elif not is_p1_adult:
        print(f'{p1_name} is not adult')
    else:
        print(f'{p2_name} is not adult')

if __name__ == '__main__':
    main()