import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

play = Player()
score= Scoreboard()
car = CarManager()

# take input
difficulty = screen.textinput("Game Level", "choose: Easy/Medium/Hard").lower()

screen.listen()
screen.onkey(play.go_up, "Up")
screen.onkey(play.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # call correct function based on difficulty
    if difficulty == "easy":
        car.rec()
    elif difficulty == "medium":
        car.rec1()
    elif difficulty == "hard":
        car.rec2()

    car.movee()
    if play.ycor() > 280:
        play.goto(0, -280)
        score.increase_level()
        car.level_up()  
    
    if car.detect_collision(play):
        game_is_on = False
        score.game_over()

screen.exitonclick()