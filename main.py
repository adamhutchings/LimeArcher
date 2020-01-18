from turtle import Screen, Turtle, bye, Terminator
from _tkinter import TclError

# Window
wn = Screen()
wn.setup(height = 800, width = 1000)
wn.title('Stupid game shit')
wn.bgcolor('#220022')
wn.tracer(0)
wn.listen()

# Goodbye
wn.onkeypress(bye, 'Escape')

try:
	while True:
		wn.update()
except (Terminator, TclError):
	pass;