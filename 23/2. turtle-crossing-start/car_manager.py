from turtle import Turtle
import random

MOVE_INCREMENT = 2   # how much speed increases each level

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [
    (280, -250), (280, -200), (280, -150), (280, -100),
    (280, -50), (280, 0), (280, 50), (280, 100),
    (280, 150), (280, 200), (280, 250)
]

list_of_car = []

class CarManager:

    def __init__(self):
        self.car_speed = 5   # initial speed

    def rec(self):  # easy
        chance = random.randint(1, 6)
        if chance <= 2:
            self.create_car()

    def rec1(self):  # medium
        chance = random.randint(1, 6)
        if chance <= 3:
            self.create_car()

    def rec2(self):  # hard
        chance = random.randint(1, 7)
        if chance <= 5:
            self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(random.choice(positions))
        list_of_car.append(new_car)

    def movee(self):
        for car in list_of_car:
            new_x = car.xcor() - self.car_speed   # 🔥 use speed variable
            car.goto(new_x, car.ycor())

    def detect_collision(self, player):
        for car in list_of_car:
            if player.distance(car) < 20:
                return True
        return False

    def level_up(self):
        self.car_speed += MOVE_INCREMENT   # 🔥 increase speed each level