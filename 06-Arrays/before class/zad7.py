import random

def create_arrays() -> None:
    print([3, 7, 1, 0, 4])
    print([[2, 3], [7, 1], [0, 4]])
    print([7 for i in range(5)])
    print([i for i in range(1, 10)])
    print([i * 2 for i in range(1, 10)])
    print([random.randint(1, 20) for i in range(10)])
    print([[] for i in range(5)])
    print([[1 for i in range(2)] for j in range(4)])
    print([[random.randint(1, 20) for i in range(3)] for j in range(5)])
    print([4, 0, 3])
    print([0 for i in range(50)])
    print([i for i in range(1, 31)])
    print([random.choice([0, 1]) for i in range(20)])
    print([[False for i in range(2)] for j in range(5)])

def main() -> None:
    create_arrays()

if __name__ == '__main__':
    main()