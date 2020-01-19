# For game objects LMAO

import turtle
from random import choice

from movement_tools import Vector

# All objects
objs = []

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
		self.gravity = True

		self.vec = Vector(0, 0)

		objs.append(self)

	# Basic movement
	def _up(self, amount):
		self.t.sety(self.t.ycor() + amount)
	def _down(self, amount):
		self.t.sety(self.t.ycor() - amount)
	def _left(self, amount):
		self.t.setx(self.t.xcor() - amount)
	def _right(self, amount):
		self.t.setx(self.t.xcor() + amount)

	# TODO: change up and down to be more specific
	def up(self):
		self.vec.y = 4
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
		self._up(self.vec.y)
		self._right(self.vec.x)

	def collided(self, other):
		if abs(self.t.xcor() - other.t.xcor()) > (self.w + other.w)*10:
			return False
		if abs(self.t.ycor() - other.t.ycor()) > (self.h + other.h)*10:
			return False

		return True

# BELOW: Subclasses of GameObject

# Obstacles for collision and whatnot

class Obstacle(GameObject):

	def __init__(self, scale, direction, color, x, y):
		if direction == 'x':
			super().__init__('square', color, scale, 1, x, y)
		elif direction == 'y':
			super().__init__('square', color, 1, scale, x, y)
		else:
			raise ValueError(f"Sorry, direction can only be x or y but was {direction} instead.")

		self.gravity = False

	def check_for_collisions(self):
		for obj in objs:
			if obj != self:
				if self.collided(obj):
					obj._down(obj.vec.y)

					# Bounces back with -0.6 velocity
					obj.vec.bounce_y(0.6)

class Projectile(GameObject):

	def __init__(self, direction, parent):
		super().__init__('circle', '#000000', 0.3, 0.3, parent.t.xcor(), parent.t.ycor())

		self.parent = parent

	def destroy(self):
		del self.t

	def check_coll(self, playersList):
		for obj in objs:
			if self.collided(obj):

				# Three cases - player, other projectile, or obstacle
				
				if obj in playersList:
					if obj != self.parent:
						obj.lives -= 1

					self.destroy()

				elif isinstance(obj, Obstacle):

					# Replacing the obstacle
					# But it can't collide with a player!
					while True:
						obj.goto(choice(range(-400, 450, 50)), choice(-300, 300, 50))

						c = False
						for player in playersList:
							if player.collided(obj):
								c = True

						if not c:
							break;

					self.destroy()

				elif isinstance(obj, Projectile):

					obj.vec.bounce_x()
					obj.vec.bounce_y()
					self.vec.bounce_x()
					self.vec.bounce_y()
