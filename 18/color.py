# import colorgram

# rgbs = []

# colors = colorgram.extract('image11.jpg', 50)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgbs.append(new_color)

# print(rgbs)



# import random
# import turtle as t

# t.colormode(255)
# tim=t.Turtle()
# color_mode=[(246, 244, 243), (233, 239, 245), (240, 245, 242), (246, 239, 241), (132, 166, 204), (220, 148, 108), (32, 41, 60), (197, 136, 149), (41, 106, 155),
#             (141, 183, 162), (164, 59, 49), (237, 212, 93), (147, 61, 68), (214, 83, 73), (52, 111, 91), (34, 61, 56), (233, 167, 159), (157, 33, 30),
#             (170, 29, 33), (15, 99, 71), (170, 189, 220), (229, 162, 166), (54, 45, 49), (57, 52, 48), (31, 60, 109), 
#             (178, 105, 115), (108, 126, 158), (175, 200, 188), (35, 150, 209), (65, 66, 56), (106, 140, 127), (163, 203, 217), (130, 129, 122), (51, 69, 71)]

# for i in range(10):
#     tim.dot(20,random.choice(color_mode))
#     tim.forward(50)

# screen=t.Screen()
# screen.exitonclick()

import random
import turtle as t

t.colormode(255)
tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_mode=[(246, 244, 243), (233, 239, 245), (240, 245, 242), (246, 239, 241), (132, 166, 204), (220, 148, 108), (32, 41, 60), (197, 136, 149), (41, 106, 155),
            (141, 183, 162), (164, 59, 49), (237, 212, 93), (147, 61, 68), (214, 83, 73), (52, 111, 91), (34, 61, 56), (233, 167, 159), (157, 33, 30),
            (170, 29, 33), (15, 99, 71), (170, 189, 220), (229, 162, 166), (54, 45, 49), (57, 52, 48), (31, 60, 109), 
            (178, 105, 115), (108, 126, 158), (175, 200, 188), (35, 150, 209), (65, 66, 56), (106, 140, 127), (163, 203, 217), (130, 129, 122), (51, 69, 71)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_mode))
    tim.forward(50)
    
    if dot_count % 10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
    
screen=t.Screen()
screen.exitonclick()