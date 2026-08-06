from tkinter import *
import os 
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 10
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(text_canva,text="00:00")
    labels.config(text="TIMER")
    tick_label.config(text="")
    global reps
    reps =0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    working_time= WORK_MIN
    short_break= SHORT_BREAK_MIN 
    long_break= LONG_BREAK_MIN 
    
    
    if reps % 8==0: 
        count_down(long_break)
        labels.config(text="LONG BREAK",fg=RED)
    elif reps % 2==0:
        count_down(short_break)
        labels.config(text="SHORT BREAK",fg=PINK)
        
    
    else:
            #for 1/3/5/7
        count_down(working_time)
        labels.config(text="WORKING TIME",fg=RED)
        
    
    
    
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    min_min=math.floor(count / 60)
    min_sec= count % 60
    if min_sec<10:
        min_sec=f"0{min_sec}"
        
    canvas.itemconfig(text_canva ,text=f"{min_min}:{min_sec }")
    if count>0:
        global timer
        timer=windows.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        working_session=math.floor(reps/2)
        for i in range(working_session):
            marks+="✅"
            tick_label.config(text=marks)


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

tick_label=Label(text="",fg=GREEN,bg=YELLOW)
tick_label.grid(column=1,row=3)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=3)


windows.mainloop()