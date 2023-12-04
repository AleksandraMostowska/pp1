# Write a program that counts the number of occurrences of any value from a tuple. 
# Sample result: Tuple: 50,20,40,50,30,50 Value: 50 Number of occurrences: 3

def main() -> None:
    my_tuple = (50, 20, 40, 50, 30, 50)
    v = 50
    print(my_tuple.count(v))

if __name__ == '__main__':
    main()