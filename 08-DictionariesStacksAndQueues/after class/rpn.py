def infix_to_rpn(expression):
    def precedence(operator):
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)

    def is_operator(token):
        return token in '+-*/^'

    def shunting_yard(tokens):
        output = []
        operators = []
        
        for token in tokens:
            if token.isnumeric():
                output.append(token)
            elif is_operator(token):
                while (operators and is_operator(operators[-1]) and
                       precedence(token) <= precedence(operators[-1])):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove the opening parenthesis

        while operators:
            output.append(operators.pop())

        return output

    tokens = expression.split()
    rpn_tokens = shunting_yard(tokens)
    return ' '.join(rpn_tokens)

# Przykład użycia:
# infix_expression = "3 + 5 * ( 2 - 1 )"
infix_expression = "3 * ( 2 + 1 ) - 5 ^ 2"
rpn_expression = infix_to_rpn(infix_expression)
print(rpn_expression)  # Wyświetli "3 5 2 1 - * +"
