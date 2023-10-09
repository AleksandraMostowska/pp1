# 45.	A natural number greater than 1 is called a prime if it has exactly 2 natural factors with 
# the values 1 and this number. Write a program that finds N leading prime numbers. 
# Read the value of N from the keyboard. Using loop statements check that the number N 
# is divisible only by 1 and by N.
# Prime numbers: 2 3 5 7 11 …

def prime_nums() -> None:
    N = int(input('Enter how many: '))
    primes = []
    cand = 2
    while len(primes) < N:
        is_prime = True
        for prime in primes:
            if cand % prime == 0:
                is_prime = False
        if is_prime:
            primes.append(cand)
        cand += 1
    
    print(' '.join(map(str, primes)))

def main() -> None:
    prime_nums()

if __name__ == '__main__':
    main()