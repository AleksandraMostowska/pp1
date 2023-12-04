# 46.	Create a function transpose_matrix(m) that returns transposed matrix m. 
# Then create a program that displays transposed matrices, in rows and columns, for the following matrices.
# a.	1 2 3
#       4 5 6
#       7 8 9

# b.	1 2 3 4 5
#       6 7 8 9 0

# c.	5 6 7 8

def transpose_matrix(m: list[list[int]]) -> None:
    for i in range(len(m)):
        for j in range(0, i):
            tmp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = tmp

def display(arr: list[list[int]]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def sth(arr):
    return [list(row) for row in zip(*arr)]

def sth2(m):
    if isinstance(m[0], list):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    
    return [[i] for i in m]


def main() -> None:
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    display(a)
    print()
    # transpose_matrix(m)
    # display(m)
    transposed = sth2(a)
    display(transposed)
    # print()
    # display(sth2(a))
    print()
    b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
    display(b)
    display(sth2(b))
    print()
    c = [5, 6, 7, 8]
    print(c)
    display(sth2(c))
    print(sth2(c))
    # transpose_matrix(c)

if __name__ == '__main__':
    main()