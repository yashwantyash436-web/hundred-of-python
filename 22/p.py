from turtle import Screen
from padd import Paddle
from myball import Balls
from score import Scoreboard
import time
import random
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

right_side = Paddle((350, 0))
left_side = Paddle((-350, 0))

ball = Balls()
score=Scoreboard()

screen.listen()
screen.onkey(right_side.go_up, "Up")
screen.onkey(right_side.go_down, "Down")


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # 🤖 AI movement (75% accuracy + slower reaction)
    if ball.xcor() < 0:  # react only when ball is on AI side

        if random.random() < 0.75:  # ✅ 75% accuracy

            if left_side.ycor() < ball.ycor():
                left_side.sety(left_side.ycor() + 7)   # slower speed
            elif left_side.ycor() > ball.ycor():
                left_side.sety(left_side.ycor() - 7)
    # Wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_side) < 50 and ball.xcor() > 320 and ball.move_x > 0:
        ball.setx(320)
        ball.bounce_x()

    if ball.distance(left_side) < 50 and ball.xcor() < -320 and ball.move_x < 0:
        ball.setx(-320)
        ball.bounce_x()
    # Miss logic
    if ball.xcor() > 380:
        ball.reset_position(direction="left")
        score.left_point()

    if ball.xcor() < -380:
        ball.reset_position(direction="right")
        score.right_point()

    if score.r_score >= 5:
        game_on = False
        score.goto(0,0)
        score.write("You  Won!", align="center", font=("Courier", 24, "normal"))

    if score.l_score >= 5:
        game_on = False
        score.goto(0,0)
        score.write("Computer Won!", align="center", font=("Courier", 24, "normal"))
            
        
screen.exitonclick()