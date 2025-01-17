# 43.	Write a program that displays the first twenty words of the Fibonacci sequence. 
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, 
# each subsequent term is the sum of the previous two. Sample result: 
# https://en.wikipedia.org/wiki/Fibonacci_number
# 0 1 1 2 3 5 8 13 21 34 ...

def display() -> str:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)
    
    # fib_seq = ''
    # for i in range(1, 21):
    #     fib_seq += str(fib(i)) + " "
    
    # return fib_seq.strip()
    
    fib_seq = []
    for i in range(1, 21):
        fib_seq.append(str(fib(i)))
    
    return ' '.join(fib_seq)

# def fib(n) -> int:
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# def dislpay_fib() -> None:
#     r = 20
#     fib_seq = []
#     for i in range(1, r + 1):
#         fib_seq.append(fib(i))
    
#     print(' '.join(map(str, fib_seq)))

def main() -> None:
    print(display())

    print(display() == '0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181')
    # print(fib(20))


if __name__ == '__main__':
    main()