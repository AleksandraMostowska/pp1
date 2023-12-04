def main() -> None:
    my_tuple = ('computation',)
    print(type(my_tuple))

    t = (10, 20, 30, 40, 50)
    reversed_t = tuple(reversed(t))
    print(reversed_t)

    print(reversed_t[1])

if __name__ == '__main__':
    main()