# 19.	Create a program that computes the second power of each array element. 
# Sample result:
# Array: 8 2 5 1 9
# 2nd power: 64 4 25 1 81
 
def getPowerOfArr(arr: [int]) -> [int]:
    return [i ** 2 for i in arr]

def main() -> None:
    print(getPowerOfArr([8, 2, 5, 1, 9]))

if __name__ == '__main__':
    main()