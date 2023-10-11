# 35.	Two numbers and an operator are given. Define a function f(number1,number2,operator) 
# that returns the result of an arithmetic operation. The available operators are +,-,*,%,**. Sample result:
# f(2,3, "+") returns 5
# f(2,3, "%") returns 2
# f(2,3, "**") returns 8
# f(2,3, "*") returns 6
# f(2,3, "-") returns -1

def f(n1: int, n2: int, operator: str) -> int | float | bool:
    match operator:
        case '+':
            return n1 + n2
        case '%':
            return n1 % n2
        case '**':
            return n1 ** n2
        case '*':
            return n1 * n2
        case '-':
            return n1 - n2
        case _:
            raise ValueError('Wrong operator')

def main() -> None:
    print(f(2, 3, "+"))
    print(f(2, 3, "%"))
    print(f(2, 3, "**"))
    print(f(2, 3, "*"))
    print(f(2, 3, "-"))

if __name__ == '__main__':
    main()