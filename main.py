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

# The floors
leftFloor   =  Obstacle(10, 'x', '#FFFFFF', -350, -250)
middleFloor =  Obstacle(10, 'x', '#FFFFFF', 0   , -250)
rightFloor  =  Obstacle(10, 'x', '#FFFFFF', 350 , -250)

# Huge ass loop
def main_game():

	while True:

		# Updating everything
		wn.update()

		# Updating objects
		for obj in objs:
			obj.tick()

			# Gravity
			if obj.gravity:
				obj.vec.affect_gravity(4, FRAMERATE)

			# Collisions with obstacles
			if isinstance(obj, Obstacle):
				obj.check_for_collisions()

			# Wraparound
			if obj.t.xcor() > 500:
				obj._left(1000)
			elif obj.t.xcor() < -500:
				obj._right(1000)

		# Death checks
		for player in [player1, player2]:
			if player.t.ycor() < -400:
				player.lives -= 1

				# Resetting motion and position
				player.t.sety(300)

				if player == player1:
					player.t.setx(-200)
				elif player == player2:
					player.t.setx(200)
				else:
					raise Exception("Uhhh... how did this happen?")

				player.vec.x = 0
				player.vec.y = 0

		# One complete iteration
		sleep(1/FRAMERATE)

try:
	main_game()

except (Terminator, TclError):
	pass;
