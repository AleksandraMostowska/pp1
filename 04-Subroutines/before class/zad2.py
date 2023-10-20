import math

def main() -> None:

    # a. Natural logarithm of 5
    log_5 = math.log(5)
    print(f"a. Natural logarithm of 5: {log_5}")

    # b. e raised to the power of 3
    e_power_3 = math.exp(3)
    print(f"b. e raised to the power of 3: {e_power_3}")

    # c. Square root of 7
    sqrt_7 = math.sqrt(7)
    print(f"c. Square root of 7: {sqrt_7}")

    # d. Sine of 90 degrees
    # The math.sin function in Python takes angles in radians, so we need to convert degrees to radians.
    angle_degrees = 90
    angle_radians = math.radians(angle_degrees)
    sine_90_degrees = math.sin(angle_radians)
    print(f"d. Sine of 90 degrees: {sine_90_degrees}")


if __name__ == '__main__':
    main()