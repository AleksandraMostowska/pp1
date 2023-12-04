# 18.	An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that displays 
# the contents of the array in reverse order. Use any loop statement. 
# Sample result:
# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

def main() -> None:
    arr = [15, 8, 31, 47, 2, 19]
    n = len(arr)

    for i in range(n - 1, 0, -1):
        print(arr[i], end=' ')

if __name__ == '__main__':
    main()