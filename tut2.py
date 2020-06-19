from tkinter import *

root = Tk()
# Width x Height
root.geometry("320x320")

# Width, Height
root.minsize(300, 200)

# Width, Height
root.maxsize(640, 640)

shakaib = Label(text="Shakaib is a good boy and this is his GUI")
shakaib.pack()

root.mainloop()
