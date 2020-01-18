# For vectors, movement-blocking, etc.

from math import sin, cos

class Vector():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def flip(self):
		self.x *= -1
		self.y *= -1

	# Rotate stuff
	def rotate(self, factor):
		newX = self.x*cos(factor) - self.y*sin(factor)
		newY = self.x*sin(factor) + self.y*cos(factor)
