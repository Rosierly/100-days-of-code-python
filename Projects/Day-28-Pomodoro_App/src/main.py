import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# App state variables
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Stop the timer and restore the UI to its initial state."""
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")

    reps = 0

    # Allow the timer to be started again
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Start the next work or break session."""
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine session type
    if reps > 0 and reps % 7 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    reps += 1

    start_button.config(state="disabled")  # disable button to prevent multiple timers


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Update the timer display and schedule the next countdown step."""
    global timer

    # Format time
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")

    # Continue countdown if time remains
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        # Stop after the long break ends
        if reps == 8:
            title_label.config(text="Done!", fg="green")
            canvas.itemconfig(timer_text, text="00:00")
            return

        # Start next session
        start_timer()

        # Update progress checkmarks
        if reps <= 8:
            work_sessions = reps // 2
            marks = ["✓" for _ in range(work_sessions)]
            check_label.config(text="".join(marks))


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=80, pady=30, bg=YELLOW)

# Title
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0, pady=5)

# Canvas (image + timer)
tomato_img = tk.PhotoImage(file="../assets/tomato.png")
img_width = tomato_img.width()
img_height = tomato_img.height()

canvas = tk.Canvas(width=img_width, height=img_height, bg=YELLOW, highlightthickness=0)
canvas.create_image(img_width // 2, img_height // 2, image=tomato_img)
timer_text = canvas.create_text(
    img_width // 2,
    img_height // 2 + 20,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 25, "bold")
)
canvas.grid(column=1, row=1, pady=10)

# Buttons
start_button = tk.Button(
    text="Start",
    width=7,
    bg=GREEN,
    fg="green",
    activebackground="green",
    activeforeground=GREEN,
    font=(FONT_NAME, 12, "bold",),
    command=start_timer
)
start_button.grid(column=0, row=2, pady=10)

reset_button = tk.Button(
    text="Reset",
    width=7,
    bg=GREEN,
    fg="green",
    activebackground="green",
    activeforeground=GREEN,
    font=(FONT_NAME, 12, "bold"),
    command=reset_timer
)
reset_button.grid(column=2, row=2, pady=10)

# Progress indicator
check_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
