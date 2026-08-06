import random
import turtle as t
screen=t.Screen()
colors=["red","blue","black","pink","orange","brown"]
positions = [(-230, -100), (-230, -60), (-230, -20), (-230, 20), (-230, 60), (-230, 100)]
all_turtles=[]

screen.setup(height=400,width=500)
user=screen.textinput(title="enter the prompt",prompt="enter the turtle color:")
print(user)


game_on=False
for i in range(6):
    new_turtle=t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(positions[i])
    all_turtles.append(new_turtle)

if user:
    game_on=True
    
while game_on:
    for turtles in all_turtles:
        if turtles.xcor()>220:
            game_on=False
            winning_color=turtles.pencolor()
            if winning_color==user:
                print(f" you won! {winning_color} win the game!")
            else:
                print(f"you lose!{winning_color} was ahead !")
            
            
        
        
        
        
        
        
        d= random.randint(0,10)
        turtles.forward(d)
        


screen.exitonclick()