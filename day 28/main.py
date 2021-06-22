from tkinter import *
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
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="D:\WORKING\programming\python\/100 days_projects\day 28\/tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2) 

timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=1, column=2)


button = Button(text="Start", highlightthickness=0)
button.grid(row=3, column=1)
button = Button(text="Reset", highlightthickness=0)
button.grid(row=3, column=3)

checkmarks = Label(text='✓',fg=GREEN, bg=YELLOW)
checkmarks.grid(row=4, column=2)

window.mainloop()