def f(arr: list[int]) -> list[int]:
    if isinstance(arr[0], list):
        return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    
    return [[i] for i in arr]

def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def main() -> None:
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
    c = [5, 6, 7, 8]

    print(a)
    print(b)
    print(c)

    print(f(a))
    print(f(b))
    print(f(c))

if __name__ == '__main__':
    main()