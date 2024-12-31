from tkinter import *

def convert_to_cm():
    inches = e.get()
    if inches.replace('.', '', 1).isdigit():
        cm = float(inches) * 2.54
        l1.config(text=f"{cm:.2f} cm")
    else:
        l1.config(text="Please enter a valid number.")

window = Tk()
window.geometry("400x400")
window.title("Inch to C.M.")

l = Label(text="Enter a number in inches below:")
l.place(x=100, y=50)
e = Entry()
e.place(x=100, y=100)
btn = Button(text="Convert", command=convert_to_cm)
btn.place(x=150, y=150)
l1 = Label(text="")
l1.place(x=100, y=200)

window.mainloop()
