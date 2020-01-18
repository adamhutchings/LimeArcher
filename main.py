from turtle import Screen, Turtle, bye, Terminator
from _tkinter import TclError

from game_object import GameObject, objs, Obstacle

from time import sleep

# Constants
FRAMERATE = 30

# Window
wn = Screen()
wn.setup(height = 800, width = 1000)
wn.title('Stupid game shit')
wn.bgcolor('#220022')
wn.tracer(0)
wn.listen()

# Goodbye to the game
wn.onkeypress(bye, 'Escape')

# Players
player1 = GameObject('circle', '#880000', 1, 1, -200, 0)
player1.binds(wn, ['w', 's', 'a', 'd'])

player2 = GameObject('square', '#008800', 1, 1, 200, 0)
player2.binds(wn, ['Up', 'Down', 'Left', 'Right'])

# Their lives
player1.lives = 3
player2.lives = 3

# The floor
floor = Obstacle(10, 'x', '#FFFFFF', 0, -250)

try:
	while True:

		# Updating everything
		wn.update()

		# Gravity
		for obj in objs:
			obj.tick()

			if obj.gravity:
				obj.vec.affect_gravity(2, FRAMERATE)

			if isinstance(obj, Obstacle):
				obj.check_for_collisions()

			for player in [player1, player2]:
				if player.t.ycor() < -400:
					player.lives -= 1

		# One complete iteration
		sleep(1/FRAMERATE)

except (Terminator, TclError):
	pass;
