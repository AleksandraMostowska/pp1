# 45.	A natural number greater than 1 is called a prime if it has exactly 2 natural factors with 
# the values 1 and this number. Write a program that finds N leading prime numbers. 
# Read the value of N from the keyboard. Using loop statements check that the number N 
# is divisible only by 1 and by N.
# Prime numbers: 2 3 5 7 11 …

# def prime_nums() -> None:
#     N = int(input('How many prime numbers: '))
#     prime_numbers = []
#     candidate = 2
#
#     while len(prime_numbers) < N:
#         is_prime = True
#         for prime in prime_numbers:
#             if candidate % prime == 0:
#                 is_prime = False
#         if is_prime:
#             prime_numbers.append(candidate)
#         candidate += 1
#
#     print(' '.join(map(str, prime_numbers)))

def prime_nums() -> str:
    N = int(input('Enter how many: '))
    primes = []

    def is_prime(n: int) -> bool:
        if n < 2:
            return False

        if n == 2 or n == 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        return True

    j = 2
    while len(primes) < N:
        if is_prime(j):
            primes.append(j)
        j += 1

    return ' '.join(map(str, primes))

def main() -> None:
    print(prime_nums())

if __name__ == '__main__':
    main()