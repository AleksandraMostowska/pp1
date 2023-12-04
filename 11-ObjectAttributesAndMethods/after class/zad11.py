# 11.	Create a class with three static methods for calculating the surface area of figures: 
# triangle, rectangle, circle. Then use these methods to calculate the area of the following figures:
# a.	Circle with a radius of 3
# b.	Rectangle with sided 4 and 7
# c.	Triangle with base 6 and height 2

import math

class AreaHandler:

    @staticmethod
    def triangle_area(base: int | float, height: int | float) -> int | float:
        return 0.5 * base * height
    
    @staticmethod
    def rectangle_area(length: int | float, width: int | float) -> int | float:
        return length * width
    
    @staticmethod
    def circle_area(radius: int | float) -> int | float:
        return math.pi * radius ** 2

def main() -> None:
    circle_radius = 3
    rectangle_length = 4
    rectangle_width = 7
    triangle_base = 6
    triangle_height = 2

    circle_area = AreaHandler.circle_area(circle_radius)
    rectangle_area = AreaHandler.rectangle_area(rectangle_length, rectangle_width)
    triangle_area = AreaHandler.triangle_area(triangle_base, triangle_height)

    print(circle_area)
    print(rectangle_area)
    print(triangle_area)

if __name__ == '__main__':
    main()