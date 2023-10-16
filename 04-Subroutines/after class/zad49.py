# 49.	The sequence of digits contains the number of points rolled with a dice. 
# Define a function f(dice) that returns a number specifying the number of dice 
# rolled the most times in a row. 
# Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice: str) -> int:
    return int(max(set(dice), key=lambda x: dice.count(x)))

def main() -> None:
    print(f("5233165554211"))
    print(f("2133"))

if __name__ == '__main__':
    main()