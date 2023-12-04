# Write a program that draws the function y = sin(x) for an angle value in the range 0-360 degrees.

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    x = list(range(0, 361, 1))
    x_radians = np.radians(x)
    y = np.sin(x_radians)

    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()