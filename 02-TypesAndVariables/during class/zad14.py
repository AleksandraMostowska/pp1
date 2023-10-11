import math

def main() -> None:
    radius = 5
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f'Area = {area}')
    print(f'Circumference: {circumference}')

if __name__ == '__main__':
    main()