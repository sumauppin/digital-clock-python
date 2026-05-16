from tkinter import *
from time import strftime

root = Tk()

root.title("Digital Clock")

root.geometry("400x200")

root.config(bg="black")


def time():

    current_time = strftime("%I:%M:%S %p")

    label.config(text=current_time)

    label.after(1000, time)


label = Label(
    root,
    font=("Arial", 40, "bold"),
    background="black",
    foreground="cyan"
)

label.pack(anchor="center", pady=50)

time()

root.mainloop()