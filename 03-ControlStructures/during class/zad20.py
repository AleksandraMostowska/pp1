# 20.	The following program calculates the sum of the integers in the range 1 to 5. Run the program in debug mode and try to analyse the program execution. 
# See how you can execute the program step by step and track changes in variable values.
# sum = 0
# for i in range(1,6):
#     print(i)
#     sum = sum + i
# print(f'Sum is {sum}')

def main() -> None:
    sum = 0
    for i in range(1,6):
        print(i)
        sum = sum + i
    print(f'Sum is {sum}')

if __name__ == '__main__':
    main()