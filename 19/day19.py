import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(15)

def move_backward():
    tim.backward(15)

def move_anticlock():
    tim.left(10)

def clock_wise():
    tim.right(10)

def clears():
    tim.clear()
screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_anticlock)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c",fun=clears)
screen.exitonclick()