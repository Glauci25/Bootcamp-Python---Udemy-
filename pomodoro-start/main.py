import tkinter
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
repeticoes = 0

# ---------------------------- TIMER RESET ------------------------------- # 
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global repeticoes

    while repeticoes < 4:
        count_down(WORK_MIN*60)
        count_down(SHORT_BREAK_MIN*60)
        repeticoes += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

espace = tkinter.Label(text=" ")
espace.grid()

canvas_img = tkinter.PhotoImage(file="/Users/estagiario.inovacao/Desktop/mundo da glau/python/pomodoro-start/tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=canvas_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(102,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = tkinter.Button(text="Iniciar", command=start)
start_button.grid(column=0, row=3)
reset_button = tkinter.Button(text="Reinicar")
reset_button.grid(column=2, row=3)

main_label = tkinter.Label(text="Tempo", font=(FONT_NAME, 40, "bold"),fg=GREEN)
main_label.config(bg=YELLOW)
main_label.grid(column=1, row=0)

espace2 = tkinter.Label(text=" ")
espace2.grid(column=1, row=2)

check_label = tkinter.Label(text="✔", font=(FONT_NAME, 20, "bold"),fg=GREEN)
check_label.config(bg=YELLOW)
check_label.grid(column=1,row=3)

window.mainloop()