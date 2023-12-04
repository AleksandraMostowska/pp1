# On the Internet, find examples of __eq__ definitions. Then complete the Point class below, 
#     describing a point on the plane with coordinates (x, y), by adding the __eq__ method to compare two points.
# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f'P({self.x},{self.y})'
# Using the Point class, create a program that calculates the distance on the plane between two defined points. 
# Using the conditional statement check if these points are identical - use the comparison operator ==, i.e. p1 == p2. 
# If the points are identical, display a message that the distance between them is 0. Otherwise, calculate 
# and display the distance between the two points.

from typing import Self


class Point():

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'P({self.x},{self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    @staticmethod
    def get_distance(p1: Self, p2: Self) -> float:
        if p1 == p2:
            return 0
        
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

def main() -> None:
    p1 = Point(2, 3)
    p2 = Point(4, 5)
    p3 = Point(5, 5)
    p4 = Point(5, 5)

    print(p1)
    print(p2)

    print(Point.get_distance(p1, p2))
    print(p3 == p4)

if __name__ == "__main__":
    main()