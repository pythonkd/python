import math


class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({0},{1})".format(self.x, self.y)

    def __bool__(self):
        print(abs(self))
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __abs__(self):
        return math.hypot(abs(self.x), abs(self.y))

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
