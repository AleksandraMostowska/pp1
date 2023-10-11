# 51.	Define a function sum(n) that for the given natural number n calculates the sum of all natural 
# numbers between 1 and n. Apply recursion. Then, create a program that calculates the sum 
# of natural numbers in the range <1,10>.

def count_sum(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return n + count_sum(n - 1)

def count_sum_in_range(range_min: int, range_max: int) -> int:
    if range_min >= range_max:
        raise ValueError('Range is not correct')
    
    return count_sum(range_max) - count_sum(range_min - 1)
    

def main() -> None:
    print(count_sum(5))
    print(count_sum(4))
    print(count_sum(10))
    print(count_sum_in_range(1, 10))

if __name__ == '__main__':
    main()