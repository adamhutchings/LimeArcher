# For vectors, movement-blocking, etc.

from math import sin, cos, atan, pi

class Vector():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def flip(self):
		self.x *= -1
		self.y *= -1

	# Rotate stuff
	# rotate the vector in radians!
	def rotate(self, factor):
		newX = self.x*cos(factor) - self.y*sin(factor)
		newY = self.x*sin(factor) + self.y*cos(factor)

		self.x = newX
		self.y = newY

	def get_angle(self):

		try:
			return atan(self.y/self.x)
		except ZeroDivisionError:
			return pi/2

	# Again - radians!
	def set_angle(self, angle):
		self.rotate(angle - self.get_angle())

	def affect_gravity(self, factor):
		self.y -= factor
