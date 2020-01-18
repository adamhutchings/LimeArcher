from turtle import Screen, Turtle, bye, Terminator
from _tkinter import TclError

from game_object import GameObject

# Window
wn = Screen()
wn.setup(height = 800, width = 1000)
wn.title('Stupid game shit')
wn.bgcolor('#220022')
wn.tracer(0)
wn.listen()

# Goodbye
wn.onkeypress(bye, 'Escape')

# Player (testing)
player1 = GameObject('circle', '#880000', 1, 1, -200, 0)
player1.binds(wn, ['w', 's', 'a', 'd'])

player2 = GameObject('square', '#008800', 1, 1, 200, 0)
player2.binds(wn, ['Up', 'Down', 'Left', 'Right'])

try:
	while True:
		wn.update()
except (Terminator, TclError):
	pass;
