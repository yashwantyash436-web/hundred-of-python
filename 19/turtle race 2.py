import random
import turtle as t

screen = t.Screen()
screen.setup(width=500, height=400)

colors = ["red", "blue"]
positions = [(-230, -100), (-230, -60), (-230, -20), (-230, 20), (-230, 60), (-230, 100)]

all_turtles = []

# two players choose colors
player1 = screen.textinput(title="Player 1", prompt=f"Choose a turtle color {colors}:")
player2 = screen.textinput(title="Player 2", prompt=f"Choose a turtle color {colors}:")

game_on = False

# create turtles
for i in range(2):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(positions[i])
    all_turtles.append(new_turtle)

# start game if both players entered something
if player1 and player2:
    game_on = True

while game_on:
    for turtle in all_turtles:

        # check winner
        if turtle.xcor() > 220:
            game_on = False
            winning_color = turtle.pencolor()

            if winning_color == player1:
                print(f"🎉 Player 1 wins! {winning_color} turtle won!")
            elif winning_color == player2:
                print(f"🎉 Player 2 wins! {winning_color} turtle won!")
            else:
                print(f"No player guessed correctly. {winning_color} turtle won!")

        # move turtle randomly
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()