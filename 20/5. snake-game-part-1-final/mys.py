import turtle as t

positions = [(0,0), (-20,0), (-40,0)]
moves = 20

UP = 90
DOWN = 270
LEFT = 180   # ❌ You wrote LEFT = 90
RIGHT = 0


class snake:
    def __init__(self):
        self.segements = []
        self.create_snake()
        self.head = self.segements[0]  
        # ❌ Your code: self.head = self.head.heading()
        # This is wrong because self.head was not defined yet.
        # We must assign the first segment as the snake head.

    def create_snake(self):
        for pos in positions:
            self.add_segment(pos)

    def add_segment(self,pos):
            shape1 = t.Turtle("square")
            shape1.color("white")
            shape1.penup()
            shape1.goto(pos)
            self.segements.append(shape1)

    def extend(self):
        self.add_segment(self.segements[-1].pos())
    
    def move(self):
        for seg in range(len(self.segements)-1, 0, -1):
            new_x = self.segements[seg - 1].xcor()
            new_y = self.segements[seg - 1].ycor()
            self.segements[seg].goto(new_x, new_y)

        self.head.forward(moves)
        # ✔ Using head is cleaner

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # ❌ Your code used self.segements[0]
            # It works, but since we defined self.head, we should use it.

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            # ❌ Your code set heading to UP instead of DOWN

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            # ❌ Your code set heading to UP

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            # ❌ Your code set heading to UP