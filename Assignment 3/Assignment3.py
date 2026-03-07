# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Jaxon Evans
# Assignment Number: Assignment 3
# Due Date: 03/06/2026
# Purpose: The objective of this program is to convert miles per gallon into kilometers
# per liter. It is a live running program so it will actively change based on the user input
# Resources: Youtube GUI examples, GeeksForGeeks was great for explaining Tkinter.
# The project is basically created around the information that I found on there


from tkinter import *

def convert(event=None):
    try:
        mpg = float(entry.get())
        result = mpg * 0.425143707
        answer.config(text=round(result,9))
    except:
        answer.config(text="")

window = Tk()
window.title("Converter")

Label(window, text="Miles Per Gallon").pack()

entry = Entry(window)
entry.pack()
entry.bind("<KeyRelease>", convert)

Label(window, text="Kilometers Per Liter").pack()

answer = Label(window, text="")
answer.pack()

window.mainloop()
