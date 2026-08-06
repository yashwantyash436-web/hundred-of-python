import random
import turtle as t
import time
from mys import snake
from food import food
from scoreboard import scorcard

tim=t.Turtle()
screen=t.Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
position=[(0,0),(-20,0),(-40,0)]
segement=[]

snake=snake()
food=food()
scorcard=scorcard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
    if snake.head.distance(food)<15:
        food.refresh()
        scorcard.increase_score()
        snake.extend()
     
    if snake.head.xcor() >280 or  snake.head.xcor() <-280 or  snake.head.ycor() >280  or  snake.head.ycor() <-280 :
        game_on=False
        scorcard.game_over()


    for segement in snake.segements[1:]:
        if snake.head.distance(segement)<10:
            game_on=False
            scorcard.game_over()
screen.exitonclick()
