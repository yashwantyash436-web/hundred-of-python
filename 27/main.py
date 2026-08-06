# from tkinter import *

# window=Tk()
# window.title("my first gui application")
# window.minsize(width=500,height=500)


# def button_clicked():
#     label.config(text="button got clicked!")

# def button_value():
#     new=input.get()
#     label.config(text=new)

# #label
# label=Label(text="GUI APPLICATION",font="Arial")
# label.grid(column=0,row=0)
# label.config(padx=50,pady=40)

# #button
# button=Button(text="Click me",command=button_value)
# button.grid(column=3,row=3)
# button.config(padx=50,pady=40)
# #new button
# new_button= Button(text="New button")
# new_button.grid(column=4,row=0)
# #entry
# input=Entry(width=10)
# print(input.get())
# input.grid(column=10,row=10)



# import turtle

# t=turtle.Turtle()
# t.write("side text")

# window.mainloop()


from tkinter import *

window=Tk()
window.title("MILE TO KILOMETER")
window.minsize(width=500,height=500)


def km_value():
    miles=float(input.get())
    km= round(miles * 1.689)
    label4.config(text=f"{km}")

#label
label1=Label(text="is equal to ",font="Arial")
label1.grid(column=0,row=5)

input=Entry(width=10)
print(input.get())
input.grid(column=1,row=2)

label2=Label(text="Miles ",font="Arial")
label2.grid(column=2,row=2)

#button
button=Button(text="Calculate",command=km_value)
button.grid(column=1,row=7)

label3=Label(text="KM ",font="Arial")
label3.grid(column=2,row=5)

label4=Label(text="0",)
label4.grid(column=1,row=5)
# #new button
# new_button= Button(text="New button")
# new_button.grid(column=4,row=0)
#entry

window.mainloop()