"""
Chapter 16 Exercises
"""
from unit_tester import test


class point:
    """creates a point object in space with x,y coordinates"""

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


# P1-5
class rectangle:
    """creates a rectangle object given the upper left corner, width, and height"""

    def __init__(self, bottom_leftcorner, width, height):

        self.bottom_leftcorner = bottom_leftcorner
        self.width = width
        self.height = height

    def __str__(self):
        return "({0}, {1}, {2})".format(self.bottom_leftcorner, self.width, self.height)

    def grow(self, delta_width=0, delta_height=0):
        self.height += delta_height
        self.width += delta_width

    def move(self, dx, dy):
        self.bottom_leftcorner.x += dx
        self.bottom_leftcorner.y += dy

    def area(self):
        area_val = self.width * self.height
        return area_val

    def perimeter(self):
        perimeter_val = (2 * self.width) + (2 * self.height)
        return perimeter_val

    def flip(self):
        self.height, self.width = self.width, self.height

    def contains(self, point_val):
        # this boolean expression checks if the point_val is contained in the bounds
        # of where the corners/endpoints of the rectangle object would be
        if (
            (point_val.x >= self.bottom_leftcorner.x)
            and (point_val.x < self.bottom_leftcorner.x + self.width)
            and (point_val.y >= self.bottom_leftcorner.y)
            and (point_val.y < self.bottom_leftcorner.y + self.height)
        ):
            return True

        else:
            return False

    def collision_detect(self, rectangle2):
        """detects if two rectangles are overlapping"""
        # define the coordinates of each corner in the given rectangle
        blc = rectangle2.bottom_leftcorner
        urc = point(
            rectangle2.bottom_leftcorner.x + rectangle2.width,
            rectangle2.bottom_leftcorner.y + rectangle2.height,
        )
        brc = point(
            rectangle2.bottom_leftcorner.x + rectangle2.width, rectangle2.height
        )
        ulc = point(
            rectangle2.bottom_leftcorner.x,
            rectangle2.bottom_leftcorner.y + rectangle2.height,
        )

        # use the contains method on each point and return True if any evalulate to True
        if (
            (self.contains(urc) == True)
            or (self.contains(ulc) == True)
            or (self.contains(brc) == True)
            or (self.contains(blc) == True)
        ):
            return True
        else:
            return False


def test_suite():
    r = rectangle(point(0, 0), 10, 5)
    print("\n P1 Area")
    test(r.area() == 50)

    print("\n P2 Perimeter")
    test(r.perimeter() == 30)

    print("\n P3 Flip")
    test(r.width == 10 and r.height == 5)
    r.flip()
    test(r.width == 5 and r.height == 10)

    print("\n P4 Contain")
    r = rectangle(point(0, 0), 10, 5)
    test(r.contains(point(0, 0)))
    test(r.contains(point(3, 3)))
    test(not r.contains(point(3, 7)))
    test(not r.contains(point(3, 5)))
    test(r.contains(point(3, 4.99999)))
    test(not r.contains(point(-3, -3)))

    print("\n P5 Collision ")
    z = rectangle(point(5, 10), 10, 10)
    y = rectangle(point(0, 20), 20, 20)
    k = rectangle(point(3, 4), 20, 20)
    s = rectangle(point(-2, -2), 5, 5)

    test(not z.collision_detect(y))
    test(y.collision_detect(z))
    test(y.collision_detect(k))
    test(k.collision_detect(y))
    test(not s.collision_detect(y))


test_suite()
