from turtle import Turtle
import random

class Balls(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_speed=0.050

        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *=0.9

    def reset_position(self, direction):
        self.goto(0, 0)
        self.move_speed =0.050

        # Random vertical direction
        self.move_y = random.choice([-10, -8, -6, 6, 8, 10])

        # Set horizontal direction
        if direction == "left":
            self.move_x = -10
            
        else:
            self.move_x = 10