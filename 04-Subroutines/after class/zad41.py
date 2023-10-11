# 41.	Define the function f(n) that returns the n-th prime number. 
# A prime number is a natural number greater than 1, divisible by 1 and that number. 
# Sample result:
# f(1) returns 2
# f(5) returns 11

def f(n: int) -> int:
    primes = []
    candidate = 2

    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
            
        if is_prime:
            primes.append(candidate)
        
        candidate += 1
    
    return primes[-1]

def main() -> None:
    print(f(1))
    print(f(5))

if __name__ == '__main__':
    main()