from tkinter import *
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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

w = Tk()
w.title("Pomodoro")
w.config(padx=100, pady=50, bg=YELLOW)
reps = 0
timer = None


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        start_counting(short_break_sec)
        l1.config(text="Short Break", fg=PINK)
    elif reps % 8 == 0:
        start_counting(long_break_sec)
        l1.config(text="Long Break", fg=RED)
    else:
        start_counting(work_sec)
        l1.config(text="WORK", fg=GREEN)


def start_counting(count):
    m = math.floor(count / 60)
    s = count % 60
    if s == 0:
        s = "00"
    elif s < 10:
        s = f"0{s}"
    canvas.itemconfig(ctext, text=f"{m}:{s}")
    if count > 0:
        global timer
        timer = w.after(1000, start_counting, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        l2.config(text=marks)


def reset():
    w.after_cancel(timer)
    canvas.itemconfig(ctext, text="00:00")
    l1.config(text="Timer", fg=GREEN)
    l2.config(text="")
    global reps
    reps = 0


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=timg)
ctext = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
l1 = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)
l1.grid(column=1, row=0)
l2 = Label(text="", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW, )
l2.grid(column=1, row=3)
b1 = Button(text="Start", highlightthickness=0, command=start_timer)
b1.grid(column=0, row=2)
b2 = Button(text="Reset", highlightthickness=0, command=reset)
b2.grid(column=2, row=2)
w.mainloop()
