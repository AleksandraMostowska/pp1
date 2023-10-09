# 38.	Write a program that creates the following pattern. Sample result:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

def main() -> None:
    for i in range(1, 10):
        print(f'{i}' * i)

if __name__ == '__main__':
    main()