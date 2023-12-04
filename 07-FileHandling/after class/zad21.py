# 21.	Create a program that saves to a text file, numbers in the range of <1,10> with their second and third power. Sample result:
# 1,1,1
# 2,4,8
# 3,9,27
# 4,16,64
# …

def save_to_file(filename: str) -> None:
    # with open(filename, 'w') as f:
    #     for i in range(1, 11):
    #         f.write(','.join([str(i ** j) for j in range(1, 4)]) + '\n')

    with open(filename, 'w') as f:
        f.write('\n'.join([(','.join([str(i ** j) for j in range(1, 4)])) for i in range(1, 11)]))

def main() -> None:
    save_to_file('powers.txt')

if __name__ == '__main__':
    main()