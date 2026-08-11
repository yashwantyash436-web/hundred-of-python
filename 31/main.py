BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

current_card = {}


try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
  global current_card, flip_timer
  windows.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  canva.itemconfig(current_text, text="French")
  canva.itemconfig(current_word, text=current_card["French"])
  # Changes the card image back to the front image
  canva.itemconfig(card_background, image=card_front_png)
  flip_timer = windows.after(1000, func=flip_function)
  


def flip_function():
  global current_card
  canva.itemconfig(current_text, text="English")
  canva.itemconfig(current_word, text=current_card["English"])
  # Changes the card image to the back image
  canva.itemconfig(card_background, image=card_back_png)
  
def is_know():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


windows = Tk()
windows.title("Playing Card")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(1000, func=flip_function)

canva = Canvas(width=800, height=526)

card_front_png = PhotoImage(file="images/card_front.png")
card_back_png = PhotoImage(
    file="images/card_back.png"
)  # Loaded the back image
card_background = canva.create_image(
    400, 263, image=card_front_png
)  # Added variable to track background
current_text = canva.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic")
)
current_word = canva.create_text(
    400, 263, text="Word", font=("ariel", 50, "bold")
)
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(row=0, column=0, columnspan=2)

flip_timer = windows.after(3000, func=flip_function)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=cross_image, highlightthickness=0, command=next_card
)
wrong_button.grid(row=1, column=0)
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(
    image=correct_image, highlightthickness=0, command=next_card
)
correct_button.grid(row=1, column=1)

next_card()
windows.mainloop()
