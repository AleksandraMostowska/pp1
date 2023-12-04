# 21.	Search he Internet and familiarise yourself with RPN (Reverse Polish Notation). 
# Then, write a program that calculates RPN expressions. RPN can be conveniently evaluated 
# using a stack structure. A user can enter by the keyboard any number, an operator (+ - * / ) or the equal sign (=). 
# a.	If the entered value is a number, push the number on to the stack
# b.	If the entered value is an operator, pop two items from the top of the stack, do the calculation, 
# and push the result of the operation on to the stack.
# c.	If the entered value is an equal sigh, pop the final result from the stack and display the result of calculation.

import stack

def RPN(expression: str) -> int:
    operators = ['+', '-', '*', '/']

    def do_action(op1: int, operator: str, op2: int) -> int:
        match operator:
            case '+':
                return op1 + op2
            case '-':
                return op1 - op2
            case '*':
                return op1 * op2
            case '/':
                try:
                    return op1 / op2 
                except:
                    raise ZeroDivisionError('Cannot divide by zero!!!')
    

    # expression_seq = expression.replace(' ', '')
    # print(expression_seq)
    for i in expression:
        if i.isdigit():
            stack.push(int(i))
        
        elif i in operators:
            if stack.check_length() < 2:
                raise ValueError('Not enough numbers to operate on.')
            
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(do_action(op1, i, op2))

        elif i == '=':
            if stack.check_length() != 1:
                raise ValueError('Invalid expression')
            result = stack.pop()
            print(result)

def main() -> None:
    # RPN('2 3 + =')
    # RPN('2 4 1 + * =')
    # RPN('2 3 + 4 5 + * =')
    RPN('8 3 1 + / 3 2 - 4 + * =')

if __name__ == '__main__':
    main()
            