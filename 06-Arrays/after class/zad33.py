# 33.	Write a program to separate even and odd numbers of a given array of integers. 
# Put all even numbers first, and then odd numbers.

def separate(arr: [int]) -> [int]:
    even = []
    odd = []
    for i in arr:
        even.append(i) if i % 2 == 0 else odd.append(i)
    
    return even + odd

def main() -> None:
    arr = [3, 9, 1, 10, 4, 8, 15, 12]
    print(separate(arr))

if __name__ == '__main__':
    main()