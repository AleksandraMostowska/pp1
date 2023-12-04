# 49.	The sequence of digits contains the number of points rolled with a dice. 
# Define a function f(dice) that returns a number specifying the number of dice 
# rolled the most times in a row. 
# Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

# def f(dice: str) -> int:
#     return int(max(set(dice), key=lambda x: dice.count(x)))

def f(dice: str) -> int:
    current_count = 1
    max_count = 1 
    most_in_row = int(dice[0])

    for i in range(len(dice) - 1):
        if dice[i] == dice[i + 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                most_in_row = int(dice[i])
        else:
            current_count = 1
    
    return most_in_row

def main() -> None:
    print(f('1122333331122112211'))
    print(f("55523531655545211111"))
    print(f("2133"))

if __name__ == '__main__':
    main()