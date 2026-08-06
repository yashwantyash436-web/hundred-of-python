from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Courier", 24, "normal"))

    def left_point(self):
        self.l_score += 1
        self.update_score()

    def right_point(self):
        self.r_score += 1
        self.update_score()