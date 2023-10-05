def main() -> None:
    a = 5 + 10 * 5
    print(f'a = {a}')

    b = 3 - 2 + 1
    print(f'b = {b}')

    c = 2 + - 3
    print(f'c = {c}')

    d = 2 ** 8
    print(f'd = {d}')

    e = 4 + 4 / 2 ** 2
    print(f'e = {e}')

    f = 4 % 3 % 2 % 1
    print(f'f = {f}')

    g = 1 + 2 % 3 ** 4 * 5
    print(f'g = {g}')

    h = True != False
    print(f'h = {h}')

    i = 2 <= 3 or False
    print(f'i = {i}')

    j = not True or not False and not True
    print(f'j = {j}')

    k = 2 < 3 and 4 < 5 or not 6 < 7
    print(f'k = {k}')

    l = 2 % 3 < 4 / 5 and 6 + 7 < 8 or not 9 + 10 == 19
    print(f'l = {l}')

    m = 0x11 + 0b11 + 11
    print(f'm = {m}')


if __name__ == '__main__':
    main()