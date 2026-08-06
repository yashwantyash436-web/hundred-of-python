# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)
    
    
# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
    
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# data=pandas.read_csv("weather_data.csv")
# print(data["day"])

# dict= data.to_dict()
# print(dict)

# lists=data["temp"].to_list()
# for i in lists:
#     print(i)
    
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# dicts= {
#     "students":["amy","abby","joel"],
#     "marks":[68,66,66]       
# }

# value=pandas.DataFrame(dicts)
# value.to_csv("new_data.csv")
# import pandas

# data=pandas.read_csv("4. 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# greyy=len(data[data["Primary Fur Color"]=="Gray"])
# red=len(data[data["Primary Fur Color"]=="Cinnamon"])
# blackk=len(data[data["Primary Fur Color"]=="Black"])
# print(greyy,red,blackk)

# dicts={
#     "fur color":["gray","red","black"]
#     ,"count":[greyy,red,blackk]
# }
# print(dicts)

# datas=pandas.DataFrame(dicts)
# datas.to_csv("filter.csv")

# def find_cor(x,y):
#     print(x,y)
    
# turtle.onscreenclick(find_cor)

# turtle.mainloop()
import turtle
import pandas

screen=turtle.Screen()
screen.title("us state list")

image="blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
state_list=data.state.to_list()
finded_state=[]

while len(finded_state)<=50:
    
    answer=screen.textinput(title=f"{len(finded_state)}/50 correct state",prompt="what are the states names ?").title()
    print(answer)
    if answer=="Exit":
        misssing_state=[]
        for states in state_list:
            if states not in finded_state:
                
                misssing_state.append(states)
        datas=pandas.DataFrame(misssing_state)
        datas.to_csv("no_state.csv")
        break
    # if answer=="Exit":
    #     missing_states=[states for states in state_list if states not in finded_state]
    #     datas=pandas.DataFrame(missing_states)
    #     datas.to_csv("no_state.csv")
        
    elif answer in state_list:
        finded_state.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        new_data=data[data.state==answer]
        t.goto(new_data.x.item(),new_data.y.item())
        t.write(answer)            
t.exitonclick()
        
#not answered by user

