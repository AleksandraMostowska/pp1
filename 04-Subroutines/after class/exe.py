def f(expression: str) -> int:
    current_num = 0
    current_op = "+"
    result = 0
    for i in expression:
        if i.isdigit():
            current_num = int(i)
        elif i in '+-':
            if current_op == "+":
                result += current_num
            else:
                result -= current_num
            
            current_num = 0
            current_op = i
    
    if current_op == "+":
        result += current_num
    else:
        result -= current_num

    return result

def main() -> None:
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))

if __name__ == '__main__':
    main()