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
leftFloor = Obstacle(10, 'x', '#FFFFFF', -350, -250)
middleFloor = Obstacle(10, 'x', '#FFFFFF', 0, -250)
rightFloor = Obstacle(10, 'x', '#FFFFFF', 350, -250)

# Walls in the middle
leftWall = Obstacle(10, 'y', '#FF2806', -270, 150)
leftMidWall = Obstacle(10, 'y', '#FF2806', -135, -50)
midWall = Obstacle(10, 'y', '#FF2806', 0, 150)
rightMidWall = Obstacle(10, 'y', '#FF2806', 135, -50)
rightWall = Obstacle(10, 'y', '#FF2806', 270, 150)


# The pen for writing things
pen = Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.color('#88FF00')


def show(text, x, y):
    pen.clear()
    pen.goto(x, y)
    pen.write(text, align = 'center', font = ('Times', 18, 'bold'))


# For, you know, dying
def death(player):

    for obj in objs:
        obj.t.hideturtle()

    show(f"Oh no! {player} died!", 0, 0)

    sleep(2)
    bye()


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

            # Bouncing off the top
            if obj.t.ycor() > 390:
                obj.vec.bounce_y(1)

        # Death checks
        for player in [player1, player2]:
            if player.t.ycor() < -400:
                player.lives -= 1

                if player.lives < 1:
                    death("Player One") if player == player1 else death("Player Two")

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
