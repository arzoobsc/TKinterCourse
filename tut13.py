from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Simple Title")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# the line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400)
can_widget.create_line(0, 400, 800, 0)

# to create a rectangle specify parameters in this order - coors of top left and coordinates of bottom right
can_widget.create_rectangle(3, 5, 700, 300, fill="blue")

can_widget.create_text(200, 200, text="python", fill="red")

can_widget.create_oval(50, 50, 244, 355)

root.mainloop()
