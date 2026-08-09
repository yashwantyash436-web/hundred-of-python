from operator import le
from tkinter import *
import os 
import random
import string
from tkinter import messagebox
import pyperclip
import json


letters=list(string.ascii_letters)
numbers=list(string.digits)
symbols=list(string.punctuation)

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    
    try:
        with open("data123.json") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="error",message="file is not there!")
    else:
        if website_entry in data:
            email=data[website_entry]["email"]
            password=data[password]["password"]
            messagebox.showinfo(title=website_entry, message=f"email: {email}\n password {password} ")
        else:
            messagebox.showinfo(title="error",message=f"no details {website_entry}")


def gen_password():
    password_list=[]
    password_list+=random.choices(letters,k=random.randint(5,6))
    password_list+=random.choices(symbols,k=random.randint(2,4))
    password_list+=random.choices(numbers,k=random.randint(2,4))

    random.shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
# def gen_password():
#     list_password=[]
#     list_password+=random.choices(letters,k=random.randint(5,6))
#     list_password+=random.choices(symbols,k=random.randint(2,4))
#     list_password+=random.choices(numbers,k=random.randint(2,4))   
    
#     random.shuffle(list_password)
#     password="".join(list_password)
#     password_entry.insert(0,password)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

 
    if len(password)==0 or  len(website)==0:
        messagebox.showinfo(title="OOPS" , message="it cannot be empty!!")
        
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

  

# ---------------------------- UI SETUP ------------------------------- #


windows= Tk()
windows.title("PASSWORD MANAGER")
windows.config(padx=50,pady=50)



canvas=Canvas(width=200 ,height=200,highlightthickness=0)

#website label#

website_label=Label(text="Website:")
website_label.grid(row=1,column=0,sticky="E")

website_entry=Entry(width=21)
website_entry.grid(row=1,column=1,columnspan=2,sticky="W")
website_entry.focus()
#----------------------------------------------------------------------#

#email label#
email_label=Label(text="Email:")
email_label.grid(row=2,column=0,sticky="W")

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky="W")
email_entry.insert(0,"yashwanth@gmail.com")

#-----------------------------------------------------------------------#


#password label#
password_label=Label(text="Password:")
password_label.grid(row=3,column=0,sticky="E")

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,sticky="W")

#------------------------------------------------------------------------#

#password button#

password_button=Button(text="Generate Password",command=gen_password)
password_button.grid(row=3,column=2,sticky="W")

add_button=Button(text="add",width=35,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

#search button#
search_button=Button(text="   Search  ",width=14,command=find_password)
search_button.grid(row=1,column=2,sticky="W")



#---------------------------------------------------------------------------#
current_dir=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_dir,"logo.png")
lock_png=PhotoImage(file=image_path)
canvas.create_image(100,100, image=lock_png)
text_canva=canvas.create_text(100,100,text="",fill="white" ,font=(FONT_NAME,35, "bold"))
canvas.grid(column=0,row=0,columnspan=3,pady=20)






windows.mainloop()