# 24.	Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
# Create a program that displays the numbers from the first array that do not appear in the second array.

def main() -> None:
    a1 = [4,36,12,28,9,44,5]
    a2 = [5,1,36]

    print([i for i in a1 if i not in a2])

if __name__ == '__main__':
    main()