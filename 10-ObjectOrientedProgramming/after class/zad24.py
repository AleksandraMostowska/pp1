# 24.	An object contains a list of coordinates of points on the plane, as a two-dimensional array. 
# Define a C class that allows you to create an object. Provide the list of coordinates of points 
# at the time of creating the object. In the class C, define a method m(n) that returns true when 
# at least n points are in the first quadrant of the coordinate system (both point coordinates 
# are greater than 0), or false otherwise. Sample result:
# C([[2,3],[1,8],[-6,4],[3,-7]])
# m(2) returns True
# m(3) returns False

from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int

    def is_in_first_quadrant(self):
        return self.x > 0 and self.y >= 0

@dataclass
class C:
    coordinates: list[Point] = field(default_factory=list)

    def m(self, n: int):
        return len([i for i in self.coordinates if i.is_in_first_quadrant()]) >= n

    @staticmethod
    def is_in_first_quadrant(point: list[int]):
        return point[0] > 0 and point[1] > 0


def main() -> None:
    p1 = Point(2, 3)
    p2 = Point(1, 8)
    p3 = Point(-6, 4)
    p4 = Point(3, -7)
    c = C([p1, p2, p3, p4])
    print(c.m(2))
    print(c.m(3))

if __name__ == '__main__':
    main()