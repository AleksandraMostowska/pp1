# 7.	Define an anonymous function that calculates the body mass index (BMI) for the given weight in kg 
# and height in cm. Then, calculate the BMI for Peter (81kg, 182cm).

def main() -> None:
    calculate_bmi = lambda h, w: (w / ((h / 100) ** 2))
    print(calculate_bmi(182, 81))

if __name__ == '__main__':
    main()