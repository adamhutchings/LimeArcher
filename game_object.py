# For game objects LMAO

import turtle
from movement_tools import Vector

class GameObject():

	def __init__(self, shape, color, width, height, x, y):
		self.t = turtle.Turtle()
		self.t.speed(0)
		self.t.penup()
		self.t.color(color)
		self.t.shape(shape)
		self.t.shapesize(stretch_len = width, stretch_wid = height)
		self.t.goto(x, y)

		self.h = height
		self.w = width

		self.vec = Vector(0, 0)

	# Basic movement
	def _up(self, amount):
		self.t.sety(self.t.ycor() + amount)
	def _down(self, amount):
		self.t.sety(self.t.ycor() - amount)
	def _left(self, amount):
		self.t.setx(self.t.xcor() - amount)
	def _right(self, amount):
		self.t.setx(self.t.xcor() + amount)

	def up(self):
		self._up(20)
	def down(self):
		self._down(20)
	def left(self):
		self._left(20)
	def right(self):
		self._right(20)

	def binds(self, wn, binds):
		wn.onkeypress(self.up, binds[0])
		wn.onkeypress(self.down, binds[1])
		wn.onkeypress(self.left, binds[2])
		wn.onkeypress(self.right, binds[3])

	# For 'moving one tick'
	def tick(self):
		self._up(self.vec[0])
		self._right(self.vec[1])
