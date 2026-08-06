from turtle import Turtle,Screen
from paddle import paddle

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("ping pong")
screen.tracer(0)
paddle=Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)

right_side= paddle((350,0))
left_side=paddle((-350,0))
screen.listen()
screen.onkey(right_side.go_up,"Up")
screen.onkey(left_side.go_down,"Down")


game_on=True

while game_on:
    screen.update()
    
    

screen.exitonclick()