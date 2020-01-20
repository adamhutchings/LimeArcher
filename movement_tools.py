# For vectors, movement-blocking, etc.

# For calculations
from math import sin, cos, atan, pi

# A vector represents a direction of movement
class Vector:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def flip(self):
        self.x *= -1
        self.y *= -1

    # Rotate stuff
    # rotate the vector in radians!
    def rotate(self, factor):
        new_x = self.x*cos(factor) - self.y*sin(factor)
        new_y = self.x*sin(factor) + self.y*cos(factor)

        self.x = new_x
        self.y = new_y

    def get_angle(self):

        try:
            return atan(self.y/self.x)
        except ZeroDivisionError:
            return pi/2

    # Again - radians!
    def set_angle(self, angle):
        self.rotate(angle - self.get_angle())

    def affect_gravity(self, factor, framerate):
        self.y -= factor/framerate

    def bounce_x(self, factor):
        self.x *= -factor

    def bounce_y(self, factor):
        self.y *= -factor
