#import os
#print(os.getcwd())
import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("flash-card-project-start/data/korean-to-portuguese.csv")
to_learn = data.to_dict(orient = "records") #transforma o csv num dicionário modelo 'records'
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Coreano")
    canvas.itemconfig(card_word, text=current_card["Coreano"])
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Português", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portugues"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)

window = Tk()
window.title("Aprendendo Coreano")
window.config(padx= 50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
img = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_bg = canvas.create_image(400,263, image=img)
card_title = canvas.create_text(400, 150, text="Coreano", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Palavra", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="flash-card-project-start/images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()
print(current_card.keys())

window.mainloop()

