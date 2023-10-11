# 40.	Define a function f(number) that returns the sum of repeated digits in a number. 
# Sample result:
# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21 

def f(number: int) -> int:
    return sum([int(i) for i in str(number) if str(number).count(i) > 1])

def main() -> None:
    print(f(1027))
    print(f(230335))
    print(f(513553007))

if __name__ == '__main__':
    main()