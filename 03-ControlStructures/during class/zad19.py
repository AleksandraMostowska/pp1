# 19.	Write a program that calculates the sum of even numbers in the range <1,10>.

def main() -> None:
    # print(sum([i for i in range(0, 11, 2)]))

    sum = 0
    for i in range(0, 11, 2):
        sum += i

    print(sum)

if __name__ == '__main__':
    main()