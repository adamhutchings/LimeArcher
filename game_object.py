# For game objects LMAO

import turtle
from random import choice

from movement_tools import Vector

# All objects
objs = []


class GameObject:

    def __init__(self, shape, color, width, height, x, y):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.color(color)
        self.t.shape(shape)
        self.t.shapesize(stretch_len=width, stretch_wid=height)
        self.t.goto(x, y)

        self.h = height
        self.w = width
        self.gravity = True

        self.vec = Vector(0, 0)

        objs.append(self)

    # Basic movement
    def up_(self, amount):
        self.t.sety(self.t.ycor() + amount)

    def down_(self, amount):
        self.t.sety(self.t.ycor() - amount)

    def left_(self, amount):
        self.t.setx(self.t.xcor() - amount)

    def right_(self, amount):
        self.t.setx(self.t.xcor() + amount)

    # Actual player movements
    def up(self):
        self.vec.y = 4

    def left(self):
        self.left_(20)

    def right(self):
        self.right_(20)

    def down(self):

        # Going though every obstacle
        # to see if it's in range
        for obj in objs:
            if isinstance(obj, Obstacle):

                # x-cor checking
                avg_wid = (self.w + obj.w)*10
                if abs(obj.t.xcor() - self.t.xcor()) < avg_wid:

                    # y-cor checking
                    avg_height = (self.h + obj.h)*10
                    y_diff = self.t.ycor() - obj.t.ycor()
                    if 100 > y_diff > avg_height:
                        self.t.sety(obj.t.ycor()+avg_height)

                        # Setting velocity to 0
                        self.vec.bounce_y(0.5)

                        # Breaking the function loop
                        return None

        # If nothing has happened
        self.t.sety(self.t.ycor()-50)
        self.vec.bounce_y(0.5)

    def binds(self, wn, binds):
        wn.onkeypress(self.up, binds[0])
        wn.onkeypress(self.down, binds[1])
        wn.onkeypress(self.left, binds[2])
        wn.onkeypress(self.right, binds[3])

    # For 'moving one tick'
    def tick(self):
        self.up_(self.vec.y)
        self.right_(self.vec.x)

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
                    obj.down_(obj.vec.y)

                    # Bounces back with -0.6 velocity
                    obj.vec.bounce_y(0.6)


class Projectile(GameObject):

    def __init__(self, parent, x, y):
        super().__init__('circle', '#000000', 0.3, 0.3, parent.t.xcor(), parent.t.ycor())

        self.parent = parent

        # Vector stuff
        self.vec.x = x
        self.vec.y = y

    def destroy(self):
        del self.t

    def check_coll(self, players_list):
        for obj in objs:
            if self.collided(obj):

                # Three cases - player, other projectile, or obstacle

                if obj in players_list:
                    if obj != self.parent:
                        obj.lives -= 1

                    self.destroy()

                elif isinstance(obj, Obstacle):

                    # Replacing the obstacle
                    # But it can't collide with a player!
                    while True:
                        obj.t.goto(choice(range(-400, 450, 50)), choice(-300, 300, 50))

                        c = False
                        for player in players_list:
                            if player.collided(obj):
                                c = True

                        if not c:
                            break

                    self.destroy()

                elif isinstance(obj, Projectile):

                    obj.vec.bounce_x(1)
                    obj.vec.bounce_y(1)
                    self.vec.bounce_x(1)
                    self.vec.bounce_y(1)
