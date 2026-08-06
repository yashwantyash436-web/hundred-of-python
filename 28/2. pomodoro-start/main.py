from tkinter import *
import os 
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
    
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    min_min=math.floor(count / 60)
    min_sec= count % 60
    if min_sec<10:
        min_sec=f"0{min_sec}"
        
    canvas.itemconfig(text_canva ,text=f"{min_min}:{min_sec }")
    if count>0:
        windows.after(1000,count_down,count-1)


# ---------------------------- UI SETUP ------------------------------- #

windows= Tk()
windows.title("Plomordo")
windows.config(padx=100 ,pady=50,bg=YELLOW)


labels=Label(text="TIMER",fg=GREEN,bg=YELLOW,highlightthickness=0,font=(FONT_NAME,35, "bold"))
labels.grid(column=0,row=1)


canvas=Canvas(width=200 ,height=224,bg=YELLOW,highlightthickness=0)

current_dir=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_dir,"tomato.png")

tomoto_png=PhotoImage(file=image_path)
canvas.create_image(100,112,  image=tomoto_png)
text_canva=canvas.create_text(100,130,text="00:00",fill="white" ,font=(FONT_NAME,35, "bold"))
canvas.grid()



start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=3)

tick_label=Label(text="✅",fg=GREEN,bg=YELLOW)
tick_label.grid(column=1,row=3)

reset_button=Button(text="Reset")
reset_button.grid(column=3,row=3)


windows.mainloop()