from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("455x244")
# photo = PhotoImage(file="1.png")

# For jpg Images
image = Image.open("1.png")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()

root.mainloop()
