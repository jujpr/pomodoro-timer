from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_periods_finished = 0
check_text = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def restart():
    global reps, check_text
    reps = 0
    check_text = ""
    window.after_cancel(timer)
    label.config(text="TIMER", fg=GREEN)
    checks.config(text=check_text)
    canvas.itemconfig(timer_text, text=f"00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, check_text
    work_time = (WORK_MIN*60)
    short_break_time = (SHORT_BREAK_MIN*60)
    long_break_time = (LONG_BREAK_MIN*60)
    reps += 1
    if reps % 8 == 0:
        check_text += CHECK_MARK
        checks.config(text=check_text)
        label.config(text="Break", fg=PINK)
        countdown(long_break_time)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        check_text += CHECK_MARK
        checks.config(text=check_text)
        label.config(text="Break", fg=PINK)
        countdown(short_break_time)
    else:
        countdown(work_time)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    mins = floor(count/60)
    if mins < 10:
        mins = f"0{mins}"
    canvas.itemconfig(timer_text, text=f"{mins}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 127, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="TIMER", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label.grid(column=1, row=0)

start = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=restart)
reset.grid(column=3, row=2)

checks = Label(text="", font=(FONT_NAME, 12, "normal"), fg=GREEN, bg=YELLOW, highlightthickness=0)
checks.grid(column=1, row=3)

window.mainloop()
