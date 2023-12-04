# 38.	A two-dimensional array of size 2 by 4 contains integer numbers. 
# Create a program that displays array values in rows and columns.

def main() -> None:
    arr = [[1, 2, 3, 4], [5, 6, 7, 8]]

    rows = 2
    cols = 4
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()