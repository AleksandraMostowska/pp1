# Write a program that draws the graph of the function f(x)=x2-3.

import matplotlib.pyplot as plt


def main() -> None:
    x = list(range(-100, 101))
    y = [i ** 2 - 3 for i in x]

    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()