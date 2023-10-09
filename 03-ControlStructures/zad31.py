# 31.	Let x and y denote the coordinates of a point on the plane. Write a program that determines in 
# which quadrant of the coordinate system the point P (x, y) is located or on which axis it is located, 
# or that it is located in the position (0,0) of the coordinate system. 
# Sample result:
# x = 5
# y = 2
# Point P(5,2) is in the first quadrant of the coordinate system

def getQuadrant() -> None:
    x = 5
    y = 2
    
    if x > 0 and y > 0:
        quadrant = 'first quadrant'
    elif x > 0 and y < 0:
        quadrant = 'fourth quadrant'
    elif x < 0 and y > 0:
        quadrant = 'second quadrant'
    elif x < 0 and y < 0:
        quadrant = 'third quadrant'
    else:
        quadrant = '(0,0) position'
    
    print(f'Point P({x},{y}) is in the {quadrant} of the coordinate system')


def main() -> None:
    getQuadrant()

if __name__ == '__main__':
    main()
    