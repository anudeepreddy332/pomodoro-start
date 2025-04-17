from tkinter import *
import math
from tkinter import PhotoImage

#CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
timer_id = None
is_paused = False
current_count = 0

#Timer mechanism
def start_timer():
    global REPS
    global is_paused
    global current_count
    if is_paused:
        is_paused = False
        start_button.config(text="Start")
        count_down(current_count)
    else:
        REPS += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if REPS % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text="Long Break",fg=RED)
        elif REPS % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Short Break",fg=PINK)
        else:
            count_down(work_sec)
            title_label.config(text="Work",fg=GREEN)


#Pause timer
def pause_timer():
    global is_paused
    global timer_id
    global current_count
    if not is_paused:
        is_paused = True
        start_button.config(text="Resume")
        window.after_cancel(timer_id)



#Reset timer
def reset_timer():
    global REPS
    window.after_cancel(timer_id)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    REPS = 0


#Countdown mechanism
def count_down(count):
    global timer_id
    global current_count
    global is_paused
    current_count = count

    count_down_min = math.floor(count/60)
    count_down_sec = count % 60
    if count_down_sec < 10:
        count_down_sec = f"0{count_down_sec}"
    canvas.itemconfig(timer_text, text=f"{count_down_min}:{count_down_sec}")
    if count > 0:
        if not is_paused:
            timer_id = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_label.config(text=marks)


#UI Setup
window = Tk()
window.config(padx=100,pady=50,bg=YELLOW)
window.title("Pomodoro")

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=201,height=224,highlightthickness=0,bg=YELLOW)
canvas.create_image(100,105,image=image)
timer_text = canvas.create_text(100,133,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",font=(FONT_NAME,20,"normal"),highlightthickness=0,borderwidth=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", font=(FONT_NAME,20,"normal"),highlightthickness=0,borderwidth=0,command=reset_timer)
reset_button.grid(row=2,column=2)

pause_button = Button(text="Pause", font=(FONT_NAME,20,"normal"),highlightthickness=0,borderwidth=0,command=pause_timer)
pause_button.grid(row=2,column=1)

title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"normal"))
title_label.grid(row=0,column=1)


check_label = Label(fg=GREEN,font=(FONT_NAME,30,"normal"),bg=YELLOW)
check_label.grid(row=3,column=1)










window.mainloop()